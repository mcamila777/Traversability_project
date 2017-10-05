#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist

def callback(msg):
	rospy.loginfo("Received a /cmd_vel message!")
	rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
	rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
	print(msg.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rosbagVelListener', anonymous=True)

    rospy.Subscriber('/cmd_vel',  Twist, callback)

	#topics:  /cmd_vel  &   /camera/rgb/image_raw

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
