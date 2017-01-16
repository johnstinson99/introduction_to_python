import matplotlib.pyplot as plt
import numpy as np


x_array = np.random.randn(1000)
plt.hist(x_array, bins=10, normed=1, histtype='bar', color='r', alpha = 0.5)


plt.savefig('my_graph.png', frameon=False, transparent=True, format='png')   # frameon=False removes the border
# plt.savefig('my_graph.pdf', frameon=False, transparent=True, format='pdf')   # frameon=False removes the border

import os
os.system('start chrome my_graph.png')