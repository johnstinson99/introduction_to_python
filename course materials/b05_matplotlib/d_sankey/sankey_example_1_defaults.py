"""Demonstrate the Sankey class by producing three basic diagrams.
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.sankey import Sankey

# Example 1 -- Mostly defaults
# This demonstrates how to create a simple diagram by implicitly calling the
# Sankey.add() method and by appending finish() to the call to the class.

# flows:
#   positive flow goes into the main stream.
#   negative flow comes out of the main stream.

# orientations:
#   0 = horizontal
#   1 = vertical upwards
#   -1 = vertical downwards

Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")

# Notice:
#   1. Axes weren't provided when Sankey() was instantiated, so they were
#      created automatically.
#   2. The scale argument wasn't necessary since the data was already
#      normalized.
#   3. By default, the lengths of the paths are justified.

plt.show()