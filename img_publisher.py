#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

cam1 = cv2.VideoCapture(2) #Left  
cam2 = cv2.VideoCapture(3) #Right
bridge = CvBridge()

def talker():
	if not cam1.isOpened():
		print("No signal camera, check the port!, try: $ ls /dev")

	pub  = rospy.Publisher('/cam_node/left',  Image, queue_size = 1)
	pub2 = rospy.Publisher('/cam_node/right', Image, queue_size = 1)
        pub3 = rospy.Publisher('/cam_node/depth', Image, queue_size = 1)
	rospy.init_node('image', anonymous = False)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		ret, frame = cam1.read()
		ret2, frame2 = cam2.read()
		if not ret:
			break

		
		msg  = bridge.cv2_to_imgmsg(frame,  "bgr8")
		msg2 = bridge.cv2_to_imgmsg(frame2, "bgr8")
                msg3 = bridge.cv2_to_imgmsg(frame3, "bgr8")
		pub.publish(msg)
		pub2.publish(msg2)
                pub3.publish(msg3)
		print("publishing Images :)")

		if cv2.waitKey(1) == ord('q'):
			break

		if rospy.is_shutdown():
			cam1.release()
			cam2.release()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
