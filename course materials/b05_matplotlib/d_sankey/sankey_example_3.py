import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey


# Example 3
# This demonstrates:
#   1. Connecting two systems
#   2. Turning off the labels of the quantities
#   3. Adding a legend
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Two Systems")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='one',
           labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th'],
           # offset=-10,
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], fc='#37c959', label='two',
           labels=[0, 'b2nd', 'b3rd'],
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend(loc='best')
# Notice that only one connection is specified, but the systems form a
# circuit since: (1) the lengths of the paths are justified and (2) the
# orientation and ordering of the flows is mirrored.

plt.show()