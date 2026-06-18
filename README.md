#  Fire and Smoke Detection using YOLOv12

## Project Overview

This project implements a **Real-Time Fire and Smoke Detection System** using **YOLOv12**, **OpenCV**, and **Python**. The model is trained to identify fire and smoke from images and videos and visualize detections with bounding boxes and confidence scores.

By leveraging the YOLOv12 object detection architecture, the system provides fast and accurate detection, making it suitable for real-time monitoring applications.

### Applications

* Forest Fire Monitoring
* CCTV Surveillance Systems
* Industrial Safety
* Smart City Infrastructure
* Early Warning Systems

---

# Project Workflow

The following notebook contains the complete training and implementation process of the Fire and Smoke Detection model:

📄 **fire_smoke_detect.ipynb**

The workflow includes:

* Dataset preparation
* YOLOv12 model training
* Validation and evaluation
* Inference on videos
* Visualization of detections

---

# Dataset

The model is trained on a custom dataset containing two classes:

| Class ID | Class Name |
| -------- | ---------- |
| 0        |  Fire    |
| 1        |  Smoke  |

---

# Features

* Real-time fire detection
* Real-time smoke detection
* Video and image support
* Bounding box visualization
* Confidence score display
* Lightweight YOLOv12 architecture
* GPU acceleration support
* Easy deployment

---

# Project Structure

```
Fire-Smoke-Detection-YOLOv12
│
├── fire_smoke.py                # Real-time detection script
├── detect_video.py              # Video prediction script
├── fire_smoke_detect.ipynb      # Training notebook
├── best.pt                      # Trained model weights
├── requirements.txt
├── README.md
│
├── video_test/
│   ├── forest_fire_test.gif
│   ├── fire-smoke-detect.mp4
│   └── fire_test.mp4
│
└── runs/
    └── detect/
```

---

# Result

The following GIF demonstrates the performance of the trained YOLOv12 model on fire and smoke videos.

![Uploading fire_smoke_detection.gif…]()




The model successfully detects:

* 🔥 Fire regions
* 🌫️ Smoke regions

and displays confidence scores for each detection.

---

# Performance

### Detection Classes

*  Fire
*  Smoke

### Inference Speed

| Device | Speed                 |
| ------ | --------------------- |
| CPU    | ~200 ms/frame         |
| GPU    | Real-time performance |

---

# Technologies Used

| Technology  | Purpose                    |
| ----------- | -------------------------- |
| Python      | Programming Language       |
| YOLOv12     | Object Detection           |
| OpenCV      | Image and Video Processing |
| Ultralytics | Training and Inference     |
| cvzone      | Bounding Box Visualization |
| NumPy       | Numerical Computation      |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Anangsha072/fire-smoke-detector.git

cd fire-smoke-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or install manually:

```bash
pip install ultralytics opencv-python cvzone numpy
```

---

# Running the Project

### Real-Time Detection

```bash
python fire_smoke.py
```

### Video Prediction

```bash
python detect_video.py
```

The output video is automatically saved inside:

```
runs/detect/predict/
```

---

# Future Improvements

* 📹 Webcam-based detection
* 🏢 CCTV surveillance integration
* 📱 Telegram alerts
* 📧 Email notifications
* 🌐 Web application deployment
* ☁️ Cloud-based monitoring
* 🤖 IoT-enabled smart fire alarm system

---

# Author

### **Anangsha Das**

Machine Learning • Deep Learning • Computer Vision

GitHub:

```
https://github.com/Anangsha072
```

---

# License

This project is open-source and available under the **MIT License**.

---

# Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support is greatly appreciated.
