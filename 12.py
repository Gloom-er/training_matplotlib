# Area chart
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 100, 1)
y = x * 2
ax.fill_between(x, y, color='skyblue', alpha=0.2)
ax.plot(x, y, color='Slateblue', alpha=0.6)
fig.show()
