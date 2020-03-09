#!/usr/bin/env python
# Client that can send a pose and recieve a solution

import sys
import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
from basic_py_scripts.srv import InverseKinematics2


def ik_client(string1, string2, posestamp):
    rospy.wait_for_service('Compute_Inverse_Kinematics2')
    try:
        handle_compute_ik2 = rospy.ServiceProxy('Compute_Inverse_Kinematics2', InverseKinematics2)
        resp1 = handle_compute_ik2(string1, string2, posestamp)
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
    poseS.pose.orientation.x = 0.2
    poseS.pose.orientation.y = 0
    poseS.pose.orientation.z = 0.4
    poseS.pose.orientation.w = 0.5
    return poseS

def usage():
    #return "%s [x y]"%sys.argv[0]
    return "placeholder"

if __name__ == "__main__":

    posestamp = generate_posestamped()
    if len(sys.argv) == 3:
        x = str(sys.argv[1])
        y = str(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting ...")
    print(100)
    print("%s => %s" % (x, ik_client(x, y, posestamp)))
