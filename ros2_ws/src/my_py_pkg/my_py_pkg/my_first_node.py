#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32   # ใช้ Int32 จริง

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')

        # ใช้ Int32
        self.publisher_ = self.create_publisher(Int32, 'chatter', 10)

        # ทุก 2 วินาที
        self.timer = self.create_timer(2.0, self.timer_callback)

        self.count = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.count   # ต้องเป็น "ตัวเลข" เท่านั้น

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: {msg.data}')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()