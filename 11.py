# boxplot
import matplotlib.pyplot as plt
import numpy as np

user_1 = [10, 3, 15, 21, 17, 14]
user_2 = [5, 13, 10, 7, 9, 12]
data = [user_1, user_2]
fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0, 0, 1, 1])

bp = ax.boxplot(data)

plt.xticks([1, 2], [user_1, user_2])
fig.show()
