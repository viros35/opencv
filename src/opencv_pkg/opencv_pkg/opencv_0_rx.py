#!/usr/bin/env python3
import cv2
import rclpy

from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class ReadTopicImg(Node):
    def __init__(self):
        super().__init__('opencv_read_node')

        self.bridgeObject = CvBridge()

        self.queueSize = 20
        self.sub = self.create_subscription(Image, 'topic_camera_image', self.img_cb, self.queueSize)

    def img_cb(self, msg):
        self.get_logger().info('img read')

        img = self.bridgeObject.imgmsg_to_cv2(msg)

        cv2.imshow('camera', img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    po = ReadTopicImg()
    rclpy.spin(po)
    po.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()