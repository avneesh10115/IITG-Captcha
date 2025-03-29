# IITG-Captcha

An automated CAPTCHA solver for the IITG website as a Firefox extension.

---

## 🚀 Demonstration

![Demo](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/example.gif?raw=true)

> **Note:** The placeholder of the field updates with an apparently incorrect answer, but this is due to the CAPTCHA updating only on the backend. The displayed response corresponds to the updated CAPTCHA.

---

## 📥 Installation

### 🔹 Release (V1.0)
1. Download the `.xpi` addon file.
2. Open `about:addons` in the Firefox browser.
3. Drag and drop the `.xpi` file.

### 🔹 Beta Version
1. Download the project files.
2. Navigate to `about:debugging` in the Firefox browser.

   ![Debugging](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img1.jpg?raw=true)

3. Select the **This Firefox** option.

   ![This Firefox](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img2.jpg?raw=true)

4. Click **Load Temporary Addon** and select `manifest.json` from the downloaded files.

   ![Load Addon](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img3.jpg?raw=true)

5. Install the necessary Python dependencies.

---

## 🔧 Usage

1. Run `extn.py` using Python to start the Flask endpoint.
   
   ![Run Flask](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/img4.jpg?raw=true)

2. Open the **IITG SSO Login Page** and enter your credentials.
3. Click on the extension icon to automatically solve the CAPTCHA.

---

## 🛠️ How It Works

### 🔹 Initial CAPTCHA Image
![Initial](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/ini1.jpg?raw=true)

### 🔹 After Color Correction
![Color Correction](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/ini2.jpg?raw=true)

### 🔹 Removing Extra Space
![Remove Space](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/ini3.jpg?raw=true)

### 🔹 Splitting CAPTCHA into Blocks
![Block 1](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block1.png?raw=true)  ![Block 2](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block2.png?raw=true)   ![Block 3](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block3.png?raw=true)  ![Block 4](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block4.png?raw=true)   ![Block 5](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block5.jpg?raw=true)   ![Block 6](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/block6.jpg?raw=true)

### 🔹 Interpretation by the Model
![Final](https://github.com/avneesh10115/IITG-Captcha/blob/main/Demo/final.jpg?raw=true)

> **Note:** `?` is sometimes misinterpreted as `7`, but this does not affect the overall result.

---

