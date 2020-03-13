#! /usr/bin/env python
# This node listens to the /joint_states topic.
import rospy
from sensor_msgs.msg import JointState

class Subscriber(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/joint_states', JointState, self.sub_callback)
        self.current_state = JointState()  # dont know yet what the message looks like

    def sub_callback(self, msg):
        self.current_state = msg

def listener():
    rospy.init_node('simple_class_node', anonymous=True)
    subscriber = Subscriber()

    print(subscriber.current_state)
    rospy.spin()

if __name__ == "__main__":
    listener()