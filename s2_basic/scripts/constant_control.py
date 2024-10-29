#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# import the message type to use
from std_msgs.msg import String


class Publisher(Node):
    def __init__(self):
				# initialize base class (must happen before everything else)
        super().__init__("Publisher_node")
        self.get_logger().info("Publisher has been created")
        self.pub = self.create_publisher(String, '/chatter', 10)
        self.timer = self.create_timer(0.1, self.publish_msg)
        self.counter = 1

    def publish_msg(self):
        msg = String()
        msg.data = f"Hello {self.counter}"
        self.pub.publish(msg)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    rclpy.shutdown()

if __name__ == "__main__":
   main()