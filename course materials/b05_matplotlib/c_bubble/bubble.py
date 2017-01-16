"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt


N = 50  # Number of bubbles
x = np.random.rand(N) # array of N random numbers
y = np.random.rand(N)
colors = np.random.rand(N)  # array of N random colours
area = np.pi * (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()