import numpy as np

# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
first_shape[1] = 5
print(first_shape)