# PSPray Rescue Robot

## 📌 Overview

This project demonstrates communication between an ESP32 microcontroller and ROS2 using micro-ROS.
Sensor data from ESP32 is transmitted over WiFi and published to a ROS2 topic, which is then read by a Python subscriber node.

---

## ⚙️ System Architecture

ESP32 → WiFi → micro-ROS Agent → ROS2 → Python Node

---

## 🚀 Features

* 📡 Send sensor data from ESP32 to ROS2
* 📊 Publish data to `/knob_value` topic
* 🖥️ Subscribe and display data using Python node
* 🌐 Wireless communication via WiFi

---

## 🧩 Technologies Used

* ROS2 (Humble)
* micro-ROS
* ESP32
* Python (rclpy)

---

## 🛠️ How to Run

### 1. Run micro-ROS Agent

```bash
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
```

### 2. Run Python Subscriber Node

```bash
ros2 run my_py_pkg my_sub
```

---

## 📂 Project Structure

```
pspray-rescue-robot/
├── firmware/        # ESP32 micro-ROS code
├── ros2_ws/
│   └── src/
│       └── my_py_pkg/   # Python ROS2 package
├── README.md
├── .gitignore
```

---

## 📈 Result

The system successfully connects ESP32 to ROS2 via WiFi.
Data published from ESP32 is received and displayed in real-time using a Python subscriber node.

Example output:

```
Received: 0
Received: 120
Received: 300
```

---

## 🎯 Purpose

This project is part of a robotics learning process focusing on:

* ROS2 communication
* Embedded systems integration
* Real-time data exchange

---

## 👤 Author

Thanakon Khodsombut
