#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# import the message type to use
from geometry_msgs.msg import Twist


class Publisher(Node):
    def __init__(self):
				# initialize base class (must happen before everything else)
        super().__init__("Publisher_node")
        self.get_logger().info("Publisher has been created")
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_vel)
        self.counter = 1

    def publish_vel(self):
        msg = Twist()  # 0 initialize everything by default
        msg.linear.x = 10  # set this to be the linear velocity
        msg.angular.z = 5 # set this to be the angular velocity
        
        self.pub.publish(msg)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    rclpy.shutdown()

if __name__ == "__main__":
   main()