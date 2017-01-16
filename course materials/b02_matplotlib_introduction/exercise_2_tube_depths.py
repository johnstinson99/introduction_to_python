#    If time - Tube lines
#    A freedom of information request here resulted in TFL publishing tube line depths
#    https://www.whatdotheyknow.com/request/depth_of_tube_lines
#
#    A CSV version of the Northern line data for this file is available in station_depths.csv
#    Import the file using csv.reader()
#    Turn the csv_reader object into a list using list()
#    Remove the title row using a slice [1:]
#    Unzip into four separate lists using a, b, c, d = zip(*my_list)
#    You need to use the asterisk here as we are unzipping a list of lists


import csv
# ADD YOUR CODE HERE



# Now plot the data. Use defaults for color to keep it simple.

import matplotlib.pyplot as plt
# ADD YOUR CODE HERE




# Add station names on the x-axis using xticks()
# Note - station_numbers is currently a list of strings.
# xticks() needs a list of integers as its first parameter.
# use the rotation='vertical' parameter

# Move the chart up vertically using subplots_adjust() so you can see the labels

# Add legend

# Add axis labels and a title

