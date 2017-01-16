import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
# x_list = [1, 2, 3, 4, 5]
# y_list = [1, 2, 3, 4, 5]
# plt.plot(x_list, y_list)

x_list = [1, 2, 3, 4, 5]
y1_list = [1, 2, 3, 4, 5]
y2_list = [2, 3, 4, 5, 6]
plt.plot(x_list, y1_list, color='r', linestyle='', marker='o')
plt.plot(x_list, y2_list, color='b', linestyle='-', linewidth=1, marker='o')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Title')

plt.xticks([1, 2, 3, 4, 5], ['AA', 'BB', 'CC', 'DD', 'EE'], rotation='vertical')
plt.margins(.2)
plt.subplots_adjust(bottom=0.15)

plt.savefig('my_graph.png', frameon=False, transparent=True, format='png')   # frameon=False removes the border
# plt.savefig('my_graph.pdf', frameon=False, transparent=True, format='pdf')   # frameon=False removes the border

import os
os.system('start chrome my_graph.png')