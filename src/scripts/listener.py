#!/usr/bin/python
import rospy
from std_msgs.msg import String
def cb(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	
def listen():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", String, cb)
	rospy.spin()
	
if __name__ == '__main__':
	listen()
