#!/usr/bin/env python
from basic_py_scripts.srv import InverseKinematics, InverseKinematicsResponse
import rospy


#from numpy.core import float64[]


def handle_compute_ik(req):
    print("Returning goal state angles")
    #print("you requested " + req)
    print(req)
    #solution = [-1.6031114799568484, -0.3187570069269499, -2.5669119402583984, -1.2030817908523226, 2.403965512561466,
    #            0.7742537749351657, -1.3350190150363965]
    solution = 1
    print(solution)
    print("3.1")
    return solution


def ik_server():
    rospy.init_node('ik_server')
    s = rospy.Service('Compute_Inverse_Kinematics', InverseKinematics, handle_compute_ik)
    print("Ready to compute Inverse Kinematics")
    rospy.spin()


if __name__ == "__main__":
    ik_server()
