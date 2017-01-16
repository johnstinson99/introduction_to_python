import random

number_of_values = 10
x_values = range(number_of_values)
y_values = random.sample(range(100), number_of_values)

# 1) Use help(random.sample) to find what the random.sample method does.
print(help(random.sample))

# 2) Add print statements to print out x_values and y_values


# 3) Create a simple plot of the x and y values,
#    using all the default values as per example_1_simple


# 4) Add color, linestyle and marker parameters
#  from the quick reference card to customise the display.
# Add axis labels and a chart title


# 5) Label the x axis 'Values' and the y axis 'Random Numbers'.
#    Give the chart the title 'Line Chart'


# 6) Put your cursor over one of the occurrences of y_values and press Shift + F6
#    Or right click on it then -> refactor -> rename.  Rename this to y1_values.
#    Note how every instance in the code changes.
#    Now create a second list of y values called y2_values using another random.sample() expression.
#    Add these to the plot, using a different set of color, linestyle and marker parameters


