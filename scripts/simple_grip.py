#!/usr/bin/env python
# Simple script to test simulate gripper

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


def talker():
    # pub = rospy.Publisher('/yumi/gripper_states', String, queue_size=10)
    gripper_r_cmd_pub = rospy.Publisher("/yumi/gripper_r_effort_cmd", Float64, queue_size=1)
    rospy.init_node('talker_grip', anonymous=True)
    rate = rospy.Rate(0.5)  # 0.5hz
    effort_command = 20

    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(effort_command)
        effort_command *= -1
        gripper_r_cmd_msg = effort_command
        gripper_r_cmd_pub.publish(effort_command)
        # pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
