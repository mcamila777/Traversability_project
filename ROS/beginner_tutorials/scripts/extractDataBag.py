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

	#Resize
	img_cols = 480
	img_rows = 360

	#Load Data
	dates = ["Oct18" , "Oct23" ]

	bagPath = []; camSavePath = []; velSavePath = []

	matchMatrixes_Path = os.path.join(expanduser("~"),'Traversability_project/imageVelDataset/timeStampsAndMatchMatrixes')

	for i in xrange(len(dates)):
	    bagPath.append( os.path.join(expanduser("~"),'Traversability_project/Segmentation_data/BAGS/regression_BAGS/test0'  + str(i+1) +'.bag') )
	    camSavePath.append( os.path.join(expanduser("~"),'Traversability_project/imageVelDataset/imagesCV2'  + dates[i]) )
	    velSavePath.append(os.path.join(expanduser("~"),'Traversability_project/imageVelDataset/vel'  + dates[i])) 

	#---------------------------------- 
	for i in xrange(0, len(dates)): 

		camTimeStampList = []
		velTimeStampList = []
		camCounter = 0
		velCounter = 0

		#hello_str = "hello world %s" % rospy.get_time()
		for topic,msg,t in rosbag.Bag(bagPath[i]).read_messages(topics=['/camera/rgb/image_raw','/cmd_vel']):
			if not rospy.is_shutdown():
				print("TimeStamp:" , t.to_sec())
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
					fileName = os.path.join(camSavePath[i], "image_" + str(camCounter) + ".jpg")
					#resize
					resized = cv2.resize(cv_image ,(img_cols, img_rows), interpolation =  cv2.INTER_CUBIC)
					#Save Cv2 image
 					cv2.imwrite(fileName, resized) #np.save( fileName, cv_image)
					camCounter = camCounter +1
					print("Image saved")
					#Acum time stamp
					camTimeStampList.append(t.to_sec())

				elif topic == '/cmd_vel':
					#print("eyyyyy '/cmd_vel'")
					#time.sleep(1.5) 
					print("msg:" , msg)

					#Save vel linear.x & angular.z
					velArray = np.array([msg.linear.x,msg.angular.z])
					fileName = os.path.join(velSavePath[i], "vel_%s" % (velCounter))
					np.save(fileName, velArray)
					velCounter = velCounter +1
					print("Vel saved")
					#Acum time stamp
					velTimeStampList.append(t.to_sec())	
		
		#bag.close()    
		#Save time stamp arrays
		fileName = os.path.join(matchMatrixes_Path, 'camTimeStampArray' + dates[i])
		np.save( fileName, np.array(camTimeStampList))
		fileName = os.path.join(matchMatrixes_Path, 'velTimeStampArray'+ dates[i])
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
