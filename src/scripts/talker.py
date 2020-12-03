#!/usr/bin/python
import rospy
from std_msgs.msg import String

def talk():
	rospy.init_node('talker', anonymous=True)
	pub = rospy.Publisher('chatter', String, queue_size=20)
	rate = rospy.Rate(5) # 5Hz
	
	while not rospy.is_shutdown():
		hello_str = "hello ROS %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talk()
	except rospy.ROSInterruptException:
		pass
