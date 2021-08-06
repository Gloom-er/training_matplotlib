# bars
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 2)

ax[0].bar([1, 2, 3], [3, 4, 5], color='red', label='vertical bar', alpha=0.8)
ax[1].barh([0.5, 1, 2.5], [0, 1, 2])
ax[0].legend(loc='best')
fig.show()