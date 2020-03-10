#!/usr/bin/env python
from basic_py_scripts.srv import InverseKinematics2, InverseKinematics2Response
from basic_py_scripts.msg import *

from std_msgs.msg import *
from geometry_msgs import *
import rospy
# Service that can accept a pose and return a solution
#from numpy.core import float64[]


def handle_compute_ik2(req):
    print("request is ")
    print(req.effector_name)
    print(req.tooltip_name)
    print(req.posestamp)
    print("Returning goal state angles")
    angles = [-1.6031114799568484, -0.3187570069269499, -2.5669119402583984, -1.2030817908523226, 2.403965512561466,
                0.7742537749351657, -1.3350190150363965]
    sol = Solution()
    sol.status = 1
    sol.ik_solution = angles
    print(sol)
    #return InverseKinematics2Response(2, solution)
    return sol

def ik_server():
    rospy.init_node('ik_server')
    s = rospy.Service('compute_ik2', InverseKinematics2, handle_compute_ik2)
    print("Ready to compute Inverse Kinematics2")
    rospy.spin()


if __name__ == "__main__":
    ik_server()
