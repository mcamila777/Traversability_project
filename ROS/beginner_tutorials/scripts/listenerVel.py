#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import numpy as np
import os
from os.path import expanduser

savePath =  os.path.join(expanduser("~"), "Traversability_project/imageVelDataset/experimentOct18")
i = 0

def callback(msg):
	global i
	
	rospy.loginfo("Received a /cmd_vel message!")
	rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
	rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
	#print(msg.data) Error: 'Twist' object has no attribute 'data'
	
	#For us in enough with  linear x,y & angular z
	#Save vel (and time stamp?)
	array = np.array([msg.linear.x,msg.linear.y,msg.angular.z])
	fileName = os.path.join(savePath, "vel_%s" % (i))
	np.save( fileName, array)
	i = i +1
	print("saved")

def listener():
    rospy.init_node('rosbagVelListener', anonymous=True)
    rospy.Subscriber('/cmd_vel',  Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
