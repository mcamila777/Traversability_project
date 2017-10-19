#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import rosbag
import time
#ROS to CV
from cv_bridge import CvBridge, CvBridgeError
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from os.path import expanduser


def extractDataBag():
	pub = rospy.Publisher('read_messages', String, queue_size=10)
	rospy.init_node('extractDataBag', anonymous=True)
	rate = rospy.Rate(10) # 10hz   #??????
	#----------------------------------
	#Variables init
	bagPath = os.path.join(expanduser("~"), "Traversability_project/Segmentation_data/BAGS/regression_BAGS/test01.bag")
	camSavePath = os.path.join(expanduser("~"),'Traversability_project/imageVelDataset/imagesOct18')
	velSavePath = os.path.join(expanduser("~"),'Traversability_project/imageVelDataset/velOct18')
	camTimeStampList = []
	velTimeStampList = []
	camCounter = 1
	velCounter = 1

	#hello_str = "hello world %s" % rospy.get_time()
	for topic,msg,t in rosbag.Bag(bagPath).read_messages(topics=['/camera/rgb/image_raw','/cmd_vel']):
		if not rospy.is_shutdown():
			print("TimeStamp:" , t)
			#sprint("topic:" , topic)

			if(topic == '/camera/rgb/image_raw'):
				#print("header:" , msg.header)
				bridge = CvBridge()
				try:	
					cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
				except CvBridgeError as e:
					print("Error")
					print(e)

				#Save image
				fileName = os.path.join(camSavePath, "image_%s" % (camCounter))
				np.save( fileName, cv_image)
				camCounter = camCounter +1
				print("Image saved")
				#Acum time stamp
				camTimeStampList.append(t)

			elif topic == '/cmd_vel':
				#print("eyyyyy '/cmd_vel'")
				#time.sleep(1.5) 
				print("msg:" , msg)

				#Save vel linear.x & angular.z
				velArray = np.array([msg.linear.x,msg.angular.z])
				fileName = os.path.join(velSavePath, "vel_%s" % (velCounter))
				np.save(fileName, velArray)
				velCounter = velCounter +1
				print("Vel saved")
				#Acum time stamp
				velTimeStampList.append(t)	
		
	#bag.close()    
	#Save time stamp arrays
	fileName = os.path.join(camSavePath, "camTimeStampArray")
	np.save( fileName, np.array(camTimeStampList))
	fileName = os.path.join(velSavePath, "velTimeStampArray")
	np.save( fileName, np.array(velTimeStampList))	 

    
	#----------------------------------
	#rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        extractDataBag()
    except rospy.ROSInterruptException:
        pass
