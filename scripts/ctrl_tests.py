# pip3 install control
# pip3 install scipy
# pip3 install matplotlib
# sudo apt-get install python3-tk
# this file is for testing control package in python, so we can later build our control system for yumi
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import control as cl
from simple_pid import PID

num = [0.5]
den = [1, 0.5]

G = cl.TransferFunction(num, den) # create Transfer Function
H = cl.TransferFunction(1,1)
pid = PID(1, 0.2, 0, 1) # setpoint = 1 # not sure if i want to use this

I = cl.feedback(G, H)

print(cl.pole(G)) #print pole
print(cl.zero(G)) #print zero


# create bode plot
# mag, phase, w = cl.bode(sys)


# plot step response
T, yout = cl.step_response(I)
plt.plot(T, yout)

# sine wave & square wave for generating reference signals
time = np.arange(0, 10, 0.1);
amplitude = np.sin(time)
# plt.plot(time, signal.square(2*np.pi*time))
# plt.plot(time, amplitude)
# show bode plot
plt.show()
