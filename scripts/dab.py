#!/usr/bin/env python
# Simple script to test simulate joint velocities

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
def talker():
    pub1r = rospy.Publisher('/yumi/joint_pos_controller_1_r/command', Float64, queue_size=1)
    pub2r = rospy.Publisher('/yumi/joint_pos_controller_2_r/command', Float64, queue_size=1)
    pub3r = rospy.Publisher('/yumi/joint_pos_controller_3_r/command', Float64, queue_size=1)
    pub4r = rospy.Publisher('/yumi/joint_pos_controller_4_r/command', Float64, queue_size=1)
    pub5r = rospy.Publisher('/yumi/joint_pos_controller_5_r/command', Float64, queue_size=1)
    pub6r = rospy.Publisher('/yumi/joint_pos_controller_6_r/command', Float64, queue_size=1)
    pub7r = rospy.Publisher('/yumi/joint_pos_controller_7_r/command', Float64, queue_size=1)

    pub1l = rospy.Publisher('/yumi/joint_pos_controller_1_l/command', Float64, queue_size=1)
    pub2l = rospy.Publisher('/yumi/joint_pos_controller_2_l/command', Float64, queue_size=1)
    pub3l = rospy.Publisher('/yumi/joint_pos_controller_3_l/command', Float64, queue_size=1)
    pub4l = rospy.Publisher('/yumi/joint_pos_controller_4_l/command', Float64, queue_size=1)
    pub5l = rospy.Publisher('/yumi/joint_pos_controller_5_l/command', Float64, queue_size=1)
    pub6l = rospy.Publisher('/yumi/joint_pos_controller_6_l/command', Float64, queue_size=1)
    pub7l = rospy.Publisher('/yumi/joint_pos_controller_7_l/command', Float64, queue_size=1)
    rospy.init_node('talker_vel', anonymous=True)
    rate = rospy.Rate(1.25) # 10hz
    pos =  0

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        pub1r.publish(0.5)
        pub2r.publish(-1)
        pub3r.publish(-1.5)
        pub4r.publish(pos)
        pub5r.publish(pos)
        pub6r.publish(pos)
        pub7r.publish(1)

        #pub1l.publish(-1.4)
        #pub2l.publish(2.1)
        pub3l.publish(1.5)
        #pub4l.publish(pos)
        #pub5l.publish(pos)
        #pub6l.publish(pos)
        #pub7l.publish(pos)


        rospy.loginfo(pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
