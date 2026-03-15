# AI-TrafficFlow-System

AI-TrafficFlow-System is an AI-powered intelligent traffic management solution that dynamically adjusts traffic signal timings based on real-time vehicle density. The system uses computer vision and adaptive signal algorithms to optimize traffic flow, reduce congestion, and improve urban mobility.

# 🚦 AI Traffic Flow Optimization System

## 📌 Overview

The **AI-TrafficFlow-System** is a smart traffic signal control system that analyzes vehicle density from images and adjusts signal timings dynamically. The system uses a deep learning-based vehicle detection model and a density-based signal switching algorithm to manage traffic efficiently at intersections.

By detecting the number of vehicles in each lane and calculating optimal signal durations, the system helps reduce traffic congestion and improve vehicle throughput.

---



**Traffic Simulation GUI**

![Simulation GUI](<detection_output (2)-3.png>)

---

## 🚀 Features

✅ **Vehicle Detection using AI:** Detects and classifies vehicles using YOLO-based object detection.
✅ **Adaptive Traffic Signal Control:** Automatically adjusts signal timings based on detected traffic density.
✅ **Traffic Simulation Interface:** Interactive traffic simulation built using Pygame.
✅ **Congestion Reduction:** Optimizes traffic flow and minimizes waiting time at intersections.
✅ **Traffic Data Logging:** Stores detection outputs and signal timing data for analysis.

---

## 🛠 Tech Stack

* **Python** – Core programming language
* **YOLOv5** – Deep learning model for vehicle detection
* **OpenCV** – Image processing and computer vision
* **Pygame** – GUI-based traffic simulation environment
* **NumPy & Pandas** – Data processing and analysis

---

## 📁 Repository Structure

```
AI-TrafficFlow-System/
│
├── output_images/            # Generated output images after detection
├── test_images/              # Input images for vehicle detection
├── FINALGUI.gif              # Demonstration of traffic simulation
├── FINAL_GUI.ipynb           # GUI simulation notebook
├── signal_calculation.ipynb  # Traffic signal timing logic
├── detection_output.png      # Example detection result
├── gui_interface.png         # GUI preview
├── README.md                 # Project documentation
└── LICENSE                   # Open-source license
```

---

## 🎯 Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/AI-TrafficFlow-System.git
cd AI-TrafficFlow-System
```

### 2️⃣ Install Required Dependencies

Make sure Python and required libraries are installed.

```
pip install notebook opencv-python numpy pandas pygame
```

### 3️⃣ Run the Project

Start Jupyter Notebook:

```
jupyter notebook
```

Then open:

```
FINAL_GUI.ipynb
```

or

```
signal_calculation.ipynb
```

Run the cells step by step to start the simulation.

---

## 📊 Results & Analysis

The system dynamically allocates signal time based on vehicle density detected in each lane.

Key outcomes from the simulation:

* **Reduced Traffic Waiting Time** during high-density conditions
* **Improved Traffic Throughput** compared to static signal systems
* **Dynamic Signal Adjustment** based on real-time vehicle counts

---

## 🔮 Future Improvements

Possible extensions for the system include:

🔹 Multi-intersection traffic coordination
🔹 Integration with IoT traffic sensors
🔹 Real-time camera feed processing
🔹 Emergency vehicle priority handling
🔹 Cloud-based traffic monitoring system

---

## 📜 License

This project is distributed under the **MIT License** for educational and research purposes.

