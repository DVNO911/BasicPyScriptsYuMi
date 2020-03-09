#!/usr/bin/env python
# Client that can send a pose and receive a solution

import sys
import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
from basic_py_scripts.srv import InverseKinematics2


def ik_client(string1, string2, posestamp):
    rospy.wait_for_service('Compute_Inverse_Kinematics2')
    print(2)
    try:
        handle_compute_ik2 = rospy.ServiceProxy('Compute_Inverse_Kinematics2', InverseKinematics2)
        print(3)
        req = basic_py_scripts.srv.InverseKinematics2Request(string1, string2, posestamp)
        print(3.1)
        resp1 = handle_compute_ik2(req)
        print(4)
        return resp1.solution
    except rospy.ServiceException:
        print("Service call failed")

 #Generate an arbitrary pose to send, will later take in arguments  
def generate_posestamped():
    poseS = PoseStamped()

    poseS.header = std_msgs.msg.Header()
    #poseS.header.stamp = rospy.Time.now()  # Note you need to call rospy.init_node() before this will work

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

    #posestamp = generate_posestamped()
    #print(posestamp)
    #print("END POSE")
    print("here")
    print(sys.argv[1])
    print("555555555555555555")
    print(sys.argv[2])
    print("!!!!!!!!!!!!!!!!!!!")
    print(sys.argv[3])
    print("and here")
    print(len(sys.argv))
    if len(sys.argv) == 4:
        x = str(sys.argv[1])
        y = str(sys.argv[2])
        posestamp = sys.argv[3]
    else:
        print(usage())
        sys.exit(1)
    print("Requesting ...")
    posestamp = generate_posestamped()
    print("%s => %s" % (x, ik_client(x, y, posestamp)))
