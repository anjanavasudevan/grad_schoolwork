import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

# Defining the general equation of circle
def circleGenerate(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

# Input parameters u and f
#Center of the circle
u = np.array(([11, 2]))
f = 25

# Radius
r = np.sqrt(LA.norm(u)**2-f)

# Generating the circle
circle = circleGenerate(u, r)

# Plotting the circle
plt.plot(circle[0,:],circle[1,:],label='$circle$')

# Marking the points
plt.annotate("(1, 2)", (1, 2), (1.1, 2))
plt.annotate("(3, -4)", (3, -4), (3.1, -4))
plt.annotate("(5, -6)", (5, -6), (5.1, -6))
plt.annotate("(11, 2)", (u[0], u[1]), (u[0]+0.1, u[1]))
plt.scatter(1,2,color='blue')
plt.scatter(3,-4,color='blue')
plt.scatter(5,-6,color='blue')
plt.scatter(u[0],u[1],color='red')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()