#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
#ROS to CV
from cv_bridge import CvBridge, CvBridgeError
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from os.path import expanduser

savePath = os.path.join(expanduser("~"), "Traversability_project/imageVelDataset/experimentOct18")
i = 0

def callback(data):
	global i
    	#rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)
	print("printing Image")
	bridge = CvBridge()

	try:	
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
	except CvBridgeError as e:
		print("Error")
		print(e)

	#Show image
	#(rows,cols,channels) = cv_image.shape
	#print("cv_image rows: ", rows, "col#s", cols)
	plt.imshow(cv_image)
	plt.show()

	#Save image and time stamp
	fileName = os.path.join(savePath, "images_%s" % (i))
	np.save( fileName, np.rollaxis(cv_image, 2))
	i = i +1
	print("saved")

def listener():

    rospy.init_node('rosbagCameraListener', anonymous=True)

    rospy.Subscriber('/camera/rgb/image_raw', Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
