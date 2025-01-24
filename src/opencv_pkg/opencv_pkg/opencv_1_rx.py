#!/usr/bin/env python3
import cv2
import rclpy

from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class ReadTopicImg(Node):
    def __init__(self):
        super().__init__('opencv_read_node')
        self.cv_bridge = CvBridge()
        
        self.sub = self.create_subscription(Image, 'topic_camera_image', self.img_cb, 20)

    def img_cb(self, img_msg):

        img = self.cv_bridge.imgmsg_to_cv2(img_msg)

        text = f'x={img.shape[1]}, y={img.shape[0]}'
        img = cv2.putText(img, text, (50,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
        img = cv2.rectangle(img, (20,20), (200,100), (255,255,255), 5)
        img = cv2.circle(img, (200,200),30,(255,255,255),5,8,0)
        img = cv2.line(img, (40,100), (200,200), (255,255,255), 5)


        self.get_logger().info('img read',throttle_duration_sec = 1)
        cv2.imshow('camera', img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ReadTopicImg()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()