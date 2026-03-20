# PSPray Rescue Robot

This project uses:
- ESP32 + micro-ROS
- ROS2 (Humble)
- Python Subscriber Node

## Features
- Read sensor data from ESP32
- Publish to ROS2 topic (/knob_value)
- Subscribe using Python node

## Run
```bash
ros2 run my_py_pkg my_sub
