import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
x_values = range(len(data))
y_values = data

plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, alpha=0.6, edgecolors='w', s=50)
plt.title("Scatter Plot of 1000 Random Numbers from a Normal Distribution", fontsize=16)
plt.xlabel("Index", fontsize=12)
plt.ylabel("Random Value", fontsize=12)
plt.grid(True)
plt.show()