#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class LShapeDriver(Node):
    def __init__(self):
        super().__init__('l_shape_driver')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # каждые 0.5 сек будет вызываться
        self.timer = self.create_timer(timer_period, self.drive)
        self.phase = 0
        self.start_time = self.get_clock().now()

    def drive(self):
        msg = Twist()
        now = self.get_clock().now()
        elapsed = (now - self.start_time).nanoseconds / 1e9  # секунды

        if self.phase == 0:
            # Едем прямо 3 секунды
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            if elapsed > 3.0:
                self.phase = 1
                self.start_time = now

        elif self.phase == 1:
            # Поворачиваем налево 90 градусов ~ 2 секунды
            msg.linear.x = 0.0
            msg.angular.z = 0.8
            if elapsed > 2.0:
                self.phase = 2
                self.start_time = now

        elif self.phase == 2:
            # Едем прямо снова
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            if elapsed > 3.0:
                self.get_logger().info('Завершено L-движение')
                rclpy.shutdown()

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LShapeDriver()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
