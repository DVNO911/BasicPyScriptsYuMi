# pip3 install control
# pip3 install matplotlib
# sudo apt-get install python3-tk
# this file is for testing control package in python, so we can later build our control system for yumi
import numpy
import matplotlib.pyplot as plt
import control as cl

num = [0.5]
den = [1, 0.5]

sys = cl.TransferFunction(num, den) #create Transfer Function
print(cl.pole(sys)) #print pole
print(cl.zero(sys)) #print zero


# create bode plot
# mag, phase, w = cl.bode(sys)


# plot step response
T, yout = cl.step_response(sys)
plt.plot(T,yout)


# show bode plot
plt.show()
