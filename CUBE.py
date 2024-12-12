import matplotlib.pyplot as plt
import numpy as np

first_5_cubes = [x**3 for x in range(1, 6)]
first_5000_cubes = [x**3 for x in range(1, 5001)]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(range(1, 6), first_5_cubes, marker='o', linestyle='-', color='blue', label='First 5 Cubes')
plt.title("First 5 Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.legend()

plt.subplot(1, 2, 2)
x_values = np.arange(1, 5001)
y_values = np.array(first_5000_cubes)
colors = y_values  # Color based on cube values

scatter = plt.scatter(x_values, y_values, c=colors, cmap='viridis', s=1)
plt.title("First 5000 Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.colorbar(scatter, label="Cube Value")

plt.tight_layout()
plt.show()
