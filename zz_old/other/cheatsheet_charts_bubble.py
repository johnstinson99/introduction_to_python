import matplotlib.pyplot as plt

x_list = [1, 2, 3, 4, 5]
# plt.plot(x_list, [1, 2, 3, 4, 5], 'rs')  # one colour and one marker symbol
# plt.plot(x_list, [2, 3, 4, 5, 6], 'b-')

# plt.xticks(x_list, ['alpha', 'bravo', 'charlie', 'delta', 'echo'], rotation='vertical')
# plt.bar([1, 2, 3, 4, 5], [1, 1, 3, 2, 4], width=0.8, color='b', linestyle='--')
# Leave margins between axes and the lines/dots
# plt.margins(.2)

# Tweak spacing to prevent clipping of tick-labels
# plt.subplots_adjust(bottom=0.15)

# Add yticks too
# plt.yticks(x_list, ['a', 'b', 'c', 'd', 'e'], rotation='vertical')


import numpy as np
import matplotlib.pyplot as plt


N = 50  # Number of bubbles
x = np.random.rand(N) # array of N random numbers
y = np.random.rand(N)
colors = np.random.rand(N)  # array of N random colours
area = np.pi * (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()

plt.savefig('my_graph.png', frameon=False, transparent=True, format='png')   # frameon=False removes the border
# plt.savefig('my_graph.pdf', frameon=False, transparent=True, format='pdf')   # frameon=False removes the border

import os
os.system('start chrome my_graph.png')