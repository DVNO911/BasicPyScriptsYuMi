#!/usr/bin/env python
# Client that can send a pose and recieve a solution

from std_msgs.msg import *
from geometry_msgs.msg import *
import sys
import rospy
from basic_py_scripts.srv import InverseKinematics


def ik_client(string):
    rospy.wait_for_service('Compute_Inverse_Kinematics')
    try:
        handle_compute_ik = rospy.ServiceProxy('Compute_Inverse_Kinematics', InverseKinematics)
        resp1 = handle_compute_ik(string)
        return resp1.solution
    except rospy.ServiceException:
        print("Service call failed")

 #Generate an arbitrary pose to send, will later take in arguments  
def generate_posestamped():
    poseS = PoseStamped()

    poseS.header = std_msgs.msg.Header()
    poseS.header.stamp = rospy.Time.now()  # Note you need to call rospy.init_node() before this will work

    poseS.pose.position.x = 1
    poseS.pose.position.y = 2
    poseS.pose.position.z = 3
    poseS.pose.orientation.x = 1
    poseS.pose.orientation.y = 1
    poseS.pose.orientation.z = 1
    poseS.pose.orientation.w = 1
def usage():
    #return "%s [x y]"%sys.argv[0]
    return "placeholder"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting ...")
    print(100)
    print("%s => %s" % (x, ik_client(x)))
