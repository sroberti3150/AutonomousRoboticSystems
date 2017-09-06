#!/usr/bin/env python
import rospy, random
from std_msgs.msg import String

def poly_talker():
	pub = rospy.Publisher("polycrier",String)
	rospy.init_node("Crier",anonymous=True)
	rate = rospy.rate(21)
	while not rospy.is_shutdown():
		number = random.randrange(1,4)
		if(number ==1):
			output = "Dean"
		elif(number == 2):
			output = "Jon"
		elif(number == 3):
			output = "Vamsi"
		rospy.loginfo(output)
		pub.publish(output)
		rate.sleep()

if __name__ == 'main':
	try:
		poly_talker()
	except:
		rospy.ROSInterruptException:
		pass
