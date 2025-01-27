#!/usr/bin/env python3
import cv2
import rclpy

from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class PublisherNodeClass(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.cameraDeviceNumber = 0
        self.camera = cv2.VideoCapture(self.cameraDeviceNumber)

        self.bridgeObject = CvBridge()
        self.topicNameFrame='topic_camera_image'

        self.queueSize = 20
        self.pub = self.create_publisher(Image, self.topicNameFrame, self.queueSize)
        self.periodCommunication =0.02

        self.timer = self.create_timer(self.periodCommunication, self.timer_cb)

        self.i = 0

    def timer_cb(self):
        success, frame = self.camera.read()

        frame = cv2.resize(frame, (820,640), interpolation=cv2.INTER_CUBIC)

        if success == True:
            img = self.bridgeObject.cv2_to_imgmsg(frame)
            self.pub.publish(img)
            self.get_logger().info(f'number = {self.i}')

            self.i += 1
        else: 
            self.get_logger().info(f'fail')




def main(args=None):
    rclpy.init(args=args)
    po = PublisherNodeClass()
    rclpy.spin(po)
    po.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
