#!/usr/bin/env python

import sys
import rospy
from basic_py_scripts.srv import InverseKinematics

def ik_client(string):
    print("1")
    rospy.wait_for_service('Compute_Inverse_Kinematics')
    print("2")
    try:
        handle_compute_ik = rospy.ServiceProxy('Compute_Inverse_Kinematics', InverseKinematics)
        resp1 = handle_compute_ik(string)
        return resp1.sum
    except rospy.ServiceException:
        print ("Service call failed")

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
    print("%s => %s" % (x, ik_client(x)))