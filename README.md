# IITG-Captcha
An automated captcha solver on the IITG website as a firefox extension


# Demonstration
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/example.gif?raw=true)

Placeholder of the field gets updated with a seemingly wrong answer but it is not the case as the captcha gets updated in only the backend and the updated captcha's response in being displayed in placeholder.

# Installation

1) Download the files.
2) Navigate to the about:debugging in firefox browser.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img1.jpg?raw=true)
3) Select the This Firefox option.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img2.jpg?raw=true)
4) Click Load Temporary Addon and select manifest.json from the downloaded files.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img3.jpg?raw=true)
5) Install the neccessary python dependencies.

# Usage

1) Run extn.py using Python to start the flask endpoint.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img4.jpg?raw=true)
2) Go to the IITG SSO Login Page and enter your login details.
3) Click on the extension to automatically solve the captcha.

# Working

## Initial Image
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/ini1.jpg?raw=true)

## After Color Correction 
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/ini2.jpg?raw=true)

## Removing Extra Space
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/ini3.jpg?raw=true)

## Splitting into blocks
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block1.png?raw=true)   ![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block2.png?raw=true)   ![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block3.png?raw=true)   ![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block4.png?raw=true)   ![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block5.jpg?raw=true)   ![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block6.jpg?raw=true)

## Interpretation By Model
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/final.jpg?raw=true)
### ? is misinterpreted as 7 but is of no consequence.


