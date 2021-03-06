#!/usr/bin/env python

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
