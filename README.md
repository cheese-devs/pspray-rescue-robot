# PSPray Rescue Robot

## Overview
This project uses ESP32 + micro-ROS to send sensor data to ROS2.

## System Architecture
ESP32 → WiFi → micro-ROS → ROS2 → Python Node

## Features
- Publish sensor data (/knob_value)
- Subscribe using Python node

## How to Run
```bash
ros2 run my_py_pkg my_sub
