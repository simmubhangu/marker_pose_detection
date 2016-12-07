#!/usr/bin/env python
import rospy
from visualization_msgs.msg import Marker

def callback(data):
    rospy.loginfo("Marker ID %s", data.id)
    
def sub():

    rospy.init_node('ID_Sub', anonymous=True)

    rospy.Subscriber("Estimated_marker", Marker, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    sub()
