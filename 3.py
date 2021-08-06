import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])

ax.plot(x, y, color='red', linestyle='-', marker='o')
ax.set_xlim(0, 11)
ax.set_ylim(-5, 10)
fig.show()
