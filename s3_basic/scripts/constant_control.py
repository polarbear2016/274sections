#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# import the message type to use
from std_msgs.msg import Int64, Bool, String
from geometry_msgs.msg import Twist

class ConstantControl(Node):
    def __init__(self) -> None:

        super().__init__("constant_control")

        self.cc_counter = 0

        self.cc_pub = self.create_publisher(Twist, "/cmd_vel", 10)
        
        self.cc_timer = self.create_timer(0.2, self.cc_callback)
        
        self.cc_emergency = self.create_subscription(Bool, "/kill", self.cc_emergency_callback, 10)

    def cc_callback(self) -> None:

        msg = Twist()  
        msg.linear.x = 0.1  
        msg.angular.z = 0.1 

        self.cc_pub.publish(msg)

        self.cc_counter += 1

    def cc_emergency_callback(self, msg: Bool) -> None:
        self.cc_timer.cancel()       
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.cc_pub.publish(msg)
        print("Emergency stop.")

        
if __name__ == "__main__":
    rclpy.init()        # initialize ROS2 context (must run before any other rclpy call)
    node = ConstantControl()  # instantiate the node
    rclpy.spin(node)    # Use ROS2 built-in schedular for executing the node
    rclpy.shutdown()    # cleanly shutdown ROS2 context