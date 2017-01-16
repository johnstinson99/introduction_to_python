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
with open('station_depths.csv', mode='r') as my_file:
    my_reader = csv.reader(my_file)
    my_list = list(my_reader)[1:]
    print(my_list)
    station_names, platform_levels, street_levels, station_numbers = zip(*my_list)
    print(station_names)

# Now plot the data. Use defaults for color to keep it simple.
import matplotlib.pyplot as plt
plt.plot(station_numbers, platform_levels, label='Platform Level')
plt.plot(station_numbers, street_levels, label='Street Level')
# plt.show()

# Add station names on the x-axis using xticks()
# Note - station_numbers is currently a list of strings.
# xticks() needs a list of integers as its first parameter.
# use the rotation='vertical' parameter
plt.xticks([int(i) for i in station_numbers], list(station_names), rotation='vertical')
# plt.show()

# Move the chart up vertically using subplots_adjust() so you can see the labels
plt.subplots_adjust(bottom=0.5)
# plt.show()

# Add legend
plt.legend(loc='upper center', shadow=True, fontsize='medium')

# Add axis labels and a title
plt.xlabel('Station')
plt.ylabel('Depth vs Sea-Level')
plt.title('Northern Line Station Depths vs Sea Level')
plt.show()
