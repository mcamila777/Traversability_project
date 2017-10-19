#!/usr/bin/env python

import message_filters
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
import cv2
from matplotlib import pyplot as plt

import std_msgs.msg
#from geometry_msgs import Twist


def callback(data):#, vel):
	print("Ey callback")

	#rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)
	rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.header.stamp)
	
	


rospy.init_node('rosbagSinc', anonymous=True)

image_sub = message_filters.Subscriber('/camera/rgb/image_raw', Image)
vel_sub = message_filters.Subscriber('/cmd_vel', Twist)

#ts = message_filters.TimeSynchronizer([image_sub ,vel_sub], 2)
ts = message_filters.TimeSynchronizer([image_sub],2)#, vel_sub], 2)
ts.registerCallback(callback)
rospy.spin()
