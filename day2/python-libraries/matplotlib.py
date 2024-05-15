import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced values from 0 to 10
y1 = np.sin(x)
y2 = np.cos(x)

# Line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='--')
plt.plot(x, y2, label='cos(x)', color='red', linestyle='-')
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title('Random Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Color Intensity')
plt.show()
