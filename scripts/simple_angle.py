#!/usr/bin/env python
# Simple script to test simulate joint velocities

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
def talker():
    pub1 = rospy.Publisher('/yumi/joint_pos_controller_1_r/command', Float64, queue_size=1)
    pub2 = rospy.Publisher('/yumi/joint_pos_controller_2_r/command', Float64, queue_size=1)
    pub3 = rospy.Publisher('/yumi/joint_pos_controller_3_r/command', Float64, queue_size=1)
    pub4 = rospy.Publisher('/yumi/joint_pos_controller_4_r/command', Float64, queue_size=1)
    pub5 = rospy.Publisher('/yumi/joint_pos_controller_5_r/command', Float64, queue_size=1)
    pub6 = rospy.Publisher('/yumi/joint_pos_controller_6_r/command', Float64, queue_size=1)
    pub7 = rospy.Publisher('/yumi/joint_pos_controller_7_r/command', Float64, queue_size=1)
    rospy.init_node('talker_vel', anonymous=True)
    rate = rospy.Rate(0.25) # 10hz
    pos =  1

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        pos*=-1
        pub1.publish(pos)
        pub2.publish(pos)
        pub3.publish(pos)
        pub4.publish(pos)
        pub5.publish(pos)
        pub6.publish(pos)
        pub7.publish(pos)

        rospy.loginfo(pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
