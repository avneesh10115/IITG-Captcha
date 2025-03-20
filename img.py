"""
    Image Processing Functions for Preprocessing the Captcha Images.
"""

from PIL import Image,ImageFilter
import numpy as np

def SplitBlocks(img):
    """
    Splits the image into operators and operands.
    """
    sections = []
    img = np.asarray(img)
    w,h = img.shape
    prev_col = 0
    flag = False
    for c in range(h):
        for r in range(w):
            if img[r,c] > 0: 
                flag = True
                break
        if not flag:
            sections.append(img[:,prev_col:c])
            prev_col = c
        flag = False
    sections.append(img[:,prev_col:h])
    main_sections = []
    for section in sections:
        if ~np.all(section == 0):
            main_sections.append(section)
        
    return [Image.fromarray(x) for x in main_sections if x.shape[1] > 5 and x.shape[0] > 5]

def rgb_to_hsv(r, g, b):
    """
        Input : (r,g,b) in range 0-255
        Output : (h,s,v) in range (0-360,0-100,0-100)
    """
    r /= 255
    g /= 255
    b /= 255
    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = 0.0+bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return np.ceil(h * 360), np.ceil(s * 100), np.ceil(v * 100)

def isBlackorWhite(s,v):
    """
    Returns True if the pixel is black or white.
    """
    return v < 25 or s < 25

def determineSaturation(s):
    return int(s > 50)

def determineVal(v):   
    """
    Returns the band based on Value (V) in HSV scale.
    Band 1: 25 < v <= 50  --> DARK
    Band 2: 50 < v <= 75  --> MILD
    Band 3: 75 < v <= 100 --> LIGHT
    
    v > 25 (cutoff) for black pixels.
    """
    if v == 100: 
        v = 99
    return (v-25) // 25 + 1
    
def AdvancedColorCorrection(image,sat_mode=False):
    """
    
    Takes input as image and selects the most used color in the image except black and white.
    Gets the list of pixels with that color , Set the major color pixels to white and rest to black.
    Uses the Hue-Saturation-Value (HSV) scale for colors.
    Works well for Black Backgrounds.
    
    Step 1 : Mode Filter to increase popularity of most used color
    Step 2 : Median Filter to remove 'Salt and Pepper' Noise
    Step 3 : Color Correction
    Step 4 : Mode Filter to remove Color Correction defects
    
    """
    
    
    HUE_RANGE  = {
        'RED': (341,360),
        'ORANGE' : (0,49),
        'YELLOW' : (50,80),
        'GREEN' : (81,150),
        'CYAN' : (151,185),
        'BLUE' : (186,250),
        'PURPLE' : (251,280),
        'PINK' : (281,320),
        'ROSE' : (321,340)
    }
    if sat_mode:
        pixel_batches = {(color,band,sat): [] for color in HUE_RANGE.keys() for band in range(1,4) for sat in range(2)}
    else:
        pixel_batches = {(color,band): [] for color in HUE_RANGE.keys() for band in range(1,4)}
    img = image.filter(ImageFilter.MedianFilter()) # .filter(ImageFilter.ModeFilter(size=3)).filter(ImageFilter.MedianFilter(size=3))
    dx,dy = img.size[::-1]
    pixel_values = np.asarray(img) # (H,S,V) for each (x,y)
    for x in range(dx):
        for y in range(dy):
            try:
                r,g,b,a = pixel_values[x,y]
            except:
                r,g,b = pixel_values[x,y]
            h,s,v = rgb_to_hsv(r,g,b)
            if isBlackorWhite(s,v):
                continue
            color = None
            for c in HUE_RANGE.keys():
                if HUE_RANGE[c][0] <= h <= HUE_RANGE[c][1]:
                    color = c
                    break
            band = determineVal(v)
            if sat_mode:
                sat = determineSaturation(s)
                pixel_batches[(color,band,sat)].append((x,y))
            else:
                pixel_batches[(color,band)].append((x,y))
            
    pixel_batches = dict(sorted(pixel_batches.items(), key=lambda item: len(item[1]), reverse=True))
    new_img = Image.new('RGB', (dx, dy), (0, 0, 0))
    for pixel in list(pixel_batches.values())[0]:
        new_img.putpixel(pixel, (255,255,255))
    new_img = new_img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90) #.filter(ImageFilter.ModeFilter()) #.filter(ImageFilter.SMOOTH).filter(ImageFilter.EDGE_ENHANCE)
    
    return new_img

def RemoveBlackSpace(image): 
    """
    Removes any rows or columns with all black pixels (not between image).
    `image` : PIL Image
    `return` : PIL Image
    """
    img = image.convert('L')
    img = np.asarray(img)
    h, w = img.shape

    for top in range(h):
        if np.any(img[top, :] == 255):
            break

    for left in range(w):
        if np.any(img[:, left] == 255):
            break

    for bottom in range(h-1, -1, -1):
        if np.any(img[bottom, :] == 255):
            break

    for right in range(w-1, -1, -1):
        if np.any(img[:, right] == 255):
            break

    img = img[top:bottom+1, left:right+1]
    return Image.fromarray(img)

def PreProcessCap(image):
    """
    Takes input as image and processes the image to make it suitable for the Neural Network.
    Output is saved at same location as input.
    
    Step 1 : Advanced Color Correction
    Step 2 : Remove Black Space
    Step 3 : Split Image into parts (Operators and Operands)
    
    ``image`` : The Image.
    `return` : Tuple of 28px * 28px images to be fed into the network
    """
    cc_img = AdvancedColorCorrection(image,False)
    bcc_img = RemoveBlackSpace(cc_img) 
    imgs = SplitBlocks(bcc_img)
        
    return [img.resize((28,28)) for img in imgs]
