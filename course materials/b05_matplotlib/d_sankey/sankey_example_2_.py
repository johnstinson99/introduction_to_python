import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# Example 2
# This demonstrates:
#   1. Setting one path longer than the others
#   2. Placing a label in the middle of the diagram
#   3. Using the scale argument to normalize the flows (scale=0.01)
#   4. Implicitly passing keyword arguments to PathPatch()
#   5. Changing the angle of the arrow heads (head_angle=180)
#   6. Changing the offset between the tips of the paths and their labels
#   7. Formatting the numbers in the path labels and the associated unit (format='%.0f', unit = '%')
#   8. Changing the appearance of the patch and the labels after the figure is
#      created
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Flow Diagram of a Widget")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='%')
sankey.add(flows=[25, 0, 60, -10, -20, -5, -15, -10, -40],
           labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th',
                   'Fifth', 'Hurray!'],
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,
                        0.25],
           patchlabel="Widget\nA",
           alpha=0.2, lw=2.0)  # Arguments to matplotlib.patches.PathPatch()
diagrams = sankey.finish()
diagrams[0].patch.set_facecolor('#37c959')
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
# Notice:
#   1. Since the sum of the flows is nonzero, the width of the trunk isn't
#      uniform.  If verbose.level is helpful (in matplotlibrc), a message is
#      given in the terminal window.
#   2. The second flow doesn't appear because its value is zero.  Again, if
#      verbose.level is helpful, a message is given in the terminal window.

plt.show()