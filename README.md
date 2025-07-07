# 👁️ Face & Eye Detection with OpenCV

This is a simple real-time face and eye detection project built using Python and OpenCV. It uses Haar Cascade Classifiers to detect faces and eyes from a webcam feed and draws bounding boxes around them.

## 🚀 Features
- Real-time face detection using webcam
- Real-time eye detection inside detected face regions
- Bounding boxes and labels on live video
- Uses pre-trained Haarcascade models provided by OpenCV

## 🛠️ Technologies Used
- Python 🐍

- OpenCV (cv2) 🖼️

- Haarcascade Classifiers from OpenCV

## 📁 File Structure

face_eye_detection/
│
├── main.py                # Main script (your code)
├── haarcascade_frontalface_default.xml # Haarcascade model for face detection
├── haarcascade_eye.xml                 # Haarcascade model for eye detection
├── README.md                           # Project documentation (this file)

## 📦 Requirements
Install OpenCV using pip:

pip install opencv-python

## ▶️ How to Run

- Clone/download the project folder
- Make sure the .xml files (Haarcascade models) are in the same directory as your script
- Run the script:
    - main.py  (A window will open showing your webcam feed with real-time detection)
- Press q to quit the application

## 🔍 How It Works
Converts each video frame to grayscale

Detects faces using haarcascade_frontalface_default.xml

If a face is detected, eyes are searched for inside that face using haarcascade_eye.xml

Bounding boxes are drawn around detected features

📌 Notes
Make sure your webcam is working properly

The detection works best in well-lit environments

You can tune the parameters like scaleFactor and minNeighbors to improve accuracy

🧠 Future Improvements
Add smile or mouth detection

Add snapshot or video saving feature

Integrate face recognition with a dataset


