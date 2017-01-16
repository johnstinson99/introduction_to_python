import matplotlib.pyplot as plt
from numpy.random import rand


for color in ['red', 'green', 'blue']:
    n = 750
    x, y = rand(2, n)  # Random values in a given shape. 2 * 750 array in this case.
    scale = 200.0 * rand(n)
    plt.scatter(x, y, c=color, s=scale, label=color,
                alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)

plt.show()