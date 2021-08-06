# Stacked bar chart
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(14, 10))
rect1 = plt.bar(np.arange(5), np.arange(5) ** 2, width=0.5, color='lightblue')

rect2 = plt.bar(np.arange(5), np.arange(5) * 2, width=0.5, color='#1f77b4')
plt.legend((rect1[0], rect2[1]), ('Support', 'Freedom'))
fig.show()
