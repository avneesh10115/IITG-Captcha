# IITG-Captcha
An automated captcha solver on the IITG website as a firefox extension

# Installation

1) Download the files.
2) Navigate to the about:debugging in firefox browser.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/img1.jpg?raw=true)
3) Select the This Firefox option.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/img2.jpg?raw=true)
4) Click Load Temporary Addon and select manifest.json from the downloaded files.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/img3.jpg?raw=true)
5) Install the neccessary python dependencies.

# Usage

1) Run extn.py using Python to start the flask endpoint.
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/img4.jpg?raw=true)
2) Go to the IITG SSO Login Page and enter your login details.
3) Click on the extension to automatically solve the captcha.

# Example
![alt-text](https://github.com/avneesh10115/IITG-Captcha/blob/main/example.gif?raw=true)

Placeholder of the field gets updated with a seemingly wrong answer but it is not the case as the captcha gets updated in only the backend and the updated captcha's response in being displayed in placeholder.
