# Кругоая диаграмма
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))
labels = 'Jan', 'Feb', 'March', 'April', 'May', 'June'
user_1 = [10, 3, 15, 21, 17, 14]
ax.pie(user_1, labels=labels, explode=(0.07, 0, 0, 0, 0, 0),
       autopct='%1.1f%%', startangle=130, shadow=True)
fig.show()
