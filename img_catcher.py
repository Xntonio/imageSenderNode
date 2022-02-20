#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

bridge = CvBridge()

class Stream:
    def __init__(self):
        self.img_L = None
        self.img_R = None
        self.img_D = None
    def image_left(self,msg):
        self.img_L = msg
        self.overlap()
    def image_right(self,msg):
        self.img_R = msg
        self.overlap()
    def image_depth(self, msg):
        self.img_D = msg
    def overlap(self):
        if self.img_R is not None and self.img_L is not None and slef.img_D is not None:
        	img_L_= bridge.imgmsg_to_cv2(self.img_L, "bgr8")
        	img_R_= bridge.imgmsg_to_cv2(self.img_R, "bgr8")
                img_D_= bridge.imgmsg_to_cv2(self.img_D, "bgr8")
        	cv2.imshow("L",img_L_)
        	cv2.imshow("R",img_R_)
                cv2.imshow("DepthMap", img_D_)
        	cv2.waitKey(1)
        	

def catcher():
	rospy.init_node('image_catcher', anonymous=True)
	stm = Stream()
	rospy.Subscriber("/cam_node/left", Image, stm.image_left)
	rospy.Subscriber("/cam_node/right",Image, stm.image_right)
        rospy.Subscriber("/cam_node/depth_map", Image, stm.image_depth)
	rospy.spin()
 
if __name__ == '__main__':
    catcher()
