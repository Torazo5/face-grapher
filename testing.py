import numpy as np
import matplotlib.pyplot as plt

x,y = map(int, input().split())
x1, y1 = map(int, input().split())

# Plot the first point with color1
plt.plot(x, y, marker='o', color='red')

# Plot the second point with color2
plt.plot(x1, y1, marker='o', color='red')

# Connect the points with a line
plt.plot([x, x1], [y, y1], color='black')

plt.show()
