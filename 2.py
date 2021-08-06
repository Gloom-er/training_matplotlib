import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])
ax.plot(x, y, marker='o')
ax.plot(0.5 * x, y, marker='^')
ax.plot(2 * x, y, marker='*')
ax.plot(x*0.3, y, color='red', linestyle='--', marker='o', alpha=0.2)
ax.plot(0.7 * x, y, '*--g', linewidth=3.5)
fig.show()
