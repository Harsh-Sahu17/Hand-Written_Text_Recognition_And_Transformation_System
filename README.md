# Handwritten Text Recognition & Transformation System  

## 📌 Overview  
This project is a **Handwritten Text Recognition & Transformation System** that converts handwritten or printed text from images into a customized handwritten style. The system allows users to upload an image, extract text using **OCR (Tesseract)**, and render the recognized text onto a new image with various font styles and customization options.  

## 🚀 Features  
- 📄 **OCR-based Text Extraction** – Uses **Tesseract OCR** to recognize text from images.  
- ✏️ **Handwriting Transformation** – Converts extracted text into a customizable handwriting style.  
- 🎨 **Customization Options** – Users can adjust font size, text color, and page color.  
- 🖼️ **Real-time Preview** – Uploaded images are displayed before processing.  
- 📂 **User-friendly Interface** – Built using **Flask, HTML, CSS, and JavaScript**.  

## 🛠️ Tech Stack  
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **OCR Engine:** Tesseract  
- **Image Processing:** Pillow (PIL)  

## 📂 Project Structure  

📁 Handwritten-Text-Recognition-Transformation │── 
📁 static │ ├── style.css │ ├── script.js │── 
📁 templates │ ├── index.html │── app.py │── requirements.txt │── README.md

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  

### 2️⃣ Install Dependencies
Ensure Python 3.x and pip are installed, then run:

pip install -r requirements.txt

### 3️⃣ Set Up Tesseract OCR
Download and install Tesseract OCR from:
🔗 Tesseract Download

Make sure to update the Tesseract path in app.py:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

### 4️⃣ Run the Application

python app.py
The app will be available at:
🔗 http://127.0.0.1:5000/

### 🎯 Usage
Upload an image with handwritten or printed text.
Choose customization options like font size, text color, and background color.
Click "Process", and the system will generate a transformed handwritten image.
Download the output image for use.

### 🐞 Troubleshooting
If Tesseract OCR is not detected, ensure the correct path is set in app.py.
If dependencies are missing, run pip install -r requirements.txt again.




