##Simple script to test simulate joint velocities

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
def talker():
    pub1 = rospy.Publisher('/yumi/joint_vel_controller_1_r/command', Float64, queue_size=1)
    pub2 = rospy.Publisher('/yumi/joint_vel_controller_2_r/command', Float64, queue_size=1)
    pub3 = rospy.Publisher('/yumi/joint_vel_controller_3_r/command', Float64, queue_size=1)
    pub4 = rospy.Publisher('/yumi/joint_vel_controller_4_r/command', Float64, queue_size=1)
    pub5 = rospy.Publisher('/yumi/joint_vel_controller_5_r/command', Float64, queue_size=1)
    pub6 = rospy.Publisher('/yumi/joint_vel_controller_6_r/command', Float64, queue_size=1)
    pub7 = rospy.Publisher('/yumi/joint_vel_controller_7_r/command', Float64, queue_size=1)
    rospy.init_node('talker_vel', anonymous=True)
    rate = rospy.Rate(0.25) # 10hz
    vel =  0.5
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        vel*=-1
        pub1.publish(vel)
        pub2.publish(vel)
        pub3.publish(vel)
        pub4.publish(vel)
        pub5.publish(vel)
        pub6.publish(vel)
        pub7.publish(vel)

        rospy.loginfo(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
