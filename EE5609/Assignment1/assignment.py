import numpy as np

# Defining input
F_vect = np.array([-1, 2, 3])
distance_vect = np.array([0, 0, 4])

# Find the work done
work = np.dot(F_vect, distance_vect)
print(work)
