import os
import numpy as np
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__), '../data/old_faithful.txt')
xs = np.loadtxt(path)

print(xs.shape)
print(xs[0])
print(xs[1])

plt.scatter(xs[:,0], xs[:,1])
plt.xlabel('Duration of eruption')
plt.ylabel('Interval between eruptions')
plt.show()

