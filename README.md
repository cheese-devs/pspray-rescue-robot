# PSPray Rescue Robot

## Overview
This project uses ESP32 with micro-ROS to send sensor data to ROS2.

## System Flow
ESP32 → WiFi → micro-ROS → ROS2 → Python Node

## Features
- Publish sensor data to /knob_value
- Subscribe using Python node

## How to Run
1. Run micro-ROS agent
2. Run ROS2 node:
   ros2 run my_py_pkg my_sub

## Project Structure
- firmware/ : ESP32 code
- ros2_ws/ : ROS2 packages
