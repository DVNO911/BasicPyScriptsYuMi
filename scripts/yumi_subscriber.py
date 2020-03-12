#! /usr/bin/env python

import rospy
from std_msgs import String


class Subscriber(object):
    def __init__(self):
        self.sub = rospy.Subscriber('yumi', String, self.sub_callback)
        self.current_angles = ()  # dont know yet what the message looks like

    def sub_callback(self, msg):
        print("---------------")
        print(self.String)
        print("-")
        print(msg)
        print("---------------")
        self.current_angles = msg



if __name__ == "__main__":
    rospy.init_node('simple_class_node', anonymous=True)
    subscriber = Subscriber()
    rospy.spin