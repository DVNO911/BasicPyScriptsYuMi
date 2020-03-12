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
Kp = 2
Ki = 0.5

num = [2.5]
den = [1, 2, 0.5]

G = cl.TransferFunction(num, den) # create Transfer Function
H = cl.TransferFunction(1,1)
PI = cl.TransferFunction([Kp, Ki], [1, 0])
print(PID)

F = cl.series(PI, G)
sys = cl.feedback(F, H)
# I = cl.feedback(G, H)
# F = cl.series(PI, I)

print(cl.pole(G)) #print pole
print(cl.zero(G)) #print zero


T = np.arange(0, 40, 0.05);
# create bode plot
# mag, phase, w = cl.bode(sys)


# plot step response
#T, yout = cl.step_response(I)
#T, yout, xout = cl.forced_response(I, T, None, 1)
#plt.plot(T, yout)

# sine wave & square wave for generating reference signals

amplitude = np.sin(T)
u = signal.square(0.1 * np.pi*T)
plt.plot(T,u)
# plt.plot(time, amplitude)



# Simulate system
T, yout, xout = cl.forced_response(sys, T, u, 0)
plt.plot(T,yout)



# show bode plot
plt.show()
