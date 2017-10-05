#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
#ROS to CV
from cv_bridge import CvBridge, CvBridgeError



def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)
	print("printing Image")
	print("CvBridge")
	bridge = CvBridge()
	print("after CvBridge")

	try:	
		print("try")
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
		print("Error")
		
		#import numpy as np
		#import os
		#Save .npy array
		#fileName = os.path.join(savePath, "images_%s" % (i))
		#np.save( fileName, np.rollaxis(image, 2))
	except CvBridgeError as e:
		print("Error")
		print(e)

	(rows,cols,channels) = cv_image.shape
	print("rows: ", rows)

def listener():

    rospy.init_node('rosbagCameraListener', anonymous=True)

    rospy.Subscriber('/camera/rgb/image_raw', Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
