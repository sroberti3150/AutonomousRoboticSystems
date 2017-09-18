#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
	rospy.init_node("listener",anonymous = True)
	rospy.Subscriber("polycrier", String, callback)
	rospy.spin()


def main():
	listener()


if __name__ == '__main__':
	main()

