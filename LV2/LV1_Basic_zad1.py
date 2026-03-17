import matplotlib.pyplot as plt
import numpy as np

plt.xlim(0, 4)
plt.ylim(0, 4)

points = np.array([[1, 1],
                   [2, 2],
                   [3, 2],
                   [3, 1],
                   [1, 1]])

x = points[:, 0]
y = points[:, 1]

plt.plot(x, y, marker='o', color='r')

#plt.show()

np.ndarray(points)