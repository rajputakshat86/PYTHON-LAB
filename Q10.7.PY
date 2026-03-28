import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.array([10, 20, 15, 25, 30])

plt.subplot(2, 2, 1)
plt.plot(x, y, 'bo-')
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.bar(x, y, color='green')
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.scatter(x, y, color='red', s=100)
plt.title("Scatter Plot")

plt.subplot(2, 2, 4)
plt.hist(np.random.randint(1, 50, 20), bins=5, color='orange', edgecolor='black')
plt.title("Histogram")

plt.tight_layout()
plt.show()