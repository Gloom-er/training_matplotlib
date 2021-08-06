import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


fig, ax = plt.subplots()


x = np.array([-3, -2, -1, 0.1, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])

ax.plot(x, y, color='red', linestyle='-', marker='o', label='y=x^2')

ax.set_xticks(np.arange(-3, 3, 0.5))
ax.set_yticks(np.arange(0, 10, 3))

ax.spines['right'].set_visible(False)
ax.grid(color='blue', linewidth=2, linestyle='--')
# Чтобы убрать сетку ax.grid()
fig.show()
# Сохранение и открытие графика
fig.savefig('./figure1.png')
img = mpimg.imread('./figure1.png')

plt.grid()
plt.imshow(img)
