#!/usr/bin/env python3
import cv2
import rclpy

from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class CamRead(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.camera = cv2.VideoCapture(0)
        self.cv_bridge = CvBridge()
        self.pub = self.create_publisher(Image, 'topic_camera_image', 20)
        self.timer = self.create_timer(0.02, self.timer_msg)
        self.i = 0

    def timer_msg(self):
        success, img = self.camera.read()
        # img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
        img = cv2.resize(img, (int(img.shape[1] / 1.5), int(img.shape[0] / 1.5)))

        if success == True:
            img_msg = self.cv_bridge.cv2_to_imgmsg(img)
            self.pub.publish(img_msg)
            self.get_logger().info(f'number = {self.i}',throttle_duration_sec = 1)
            self.i += 1
        else:
            self.get_logger().warn(f'fail', throttle_duration_sec = 1)

def main(args=None):
    rclpy.init(args=args)
    node = CamRead()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
