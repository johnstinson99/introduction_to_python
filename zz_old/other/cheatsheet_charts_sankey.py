import matplotlib.pyplot as plt
import numpy as np
from matplotlib.sankey import Sankey


Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()

plt.savefig('my_graph.png', frameon=False, transparent=True, format='png')   # frameon=False removes the border
# plt.savefig('my_graph.pdf', frameon=False, transparent=True, format='pdf')   # frameon=False removes the border

import os
os.system('start chrome my_graph.png')