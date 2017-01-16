import matplotlib.pyplot as plt
import math

# Create a list of x values from 1 to 20 in increments of 0.01.
# Range only accepts ints
# so we first need to create a range of 0 to 2000
# and divide each number by 100.
x_list_floats = [x/100.0 for x in range(0, 2000)]

# Now create a list of y values.
# take sin(x) for each x value in x_list_floats
y_list = [math.sin(x) for x in x_list_floats]

plt.plot(x_list_floats, y_list)  # note - don't try x=x_list_floats, y=y_list. It doesn't work.

plt.show()
