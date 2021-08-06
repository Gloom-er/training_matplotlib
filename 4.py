import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.array([-3, -2, -1, 0.1, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])

ax.plot(x, y, color='red', linestyle='-', marker='o', label='y=x^2')

ax.plot(0.5*x, y, color='green', linestyle='-', marker='*', label='y=0.5 * x^2')
ax.set_title('Заголовок моего графика', fontsize=20)
ax.set_xlabel('Ось х')
ax.set_ylabel('Ось y')
ax.legend(loc='lower left')
fig.show()
