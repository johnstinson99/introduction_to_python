from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


def get_sealevel_data_from_url(my_url):
    html = urlopen(my_url).read()
    # print(html)
    html_string = str(BeautifulSoup(html, 'html.parser'))
    # print(html_string)
    my_list = html_string.split('\n')
    # print(my_list)
    # print(soup.prettify())
    reader = csv.reader(my_list, delimiter=';')
    # for row in reader:
    #     print(row)
    int_list = [[int(row[0]), int(row[1])] for row in reader
                if len(row) > 1   # remove empty rows
                and int(row[1]) != -99999]  # remove years and values with -99999 values
    # print(int_list)
    list_of_tuples = list(zip(*int_list))
    x_list = list(list_of_tuples[0])
    y_list = list(list_of_tuples[1])
    # y_list = [np.nan if y == -99999 else y for y in y_list_raw]
    two_lists = [x_list, y_list]
    # print(two_lists)
    return two_lists

my_data = get_sealevel_data_from_url("http://www.psmsl.org/data/obtaining/rlr.annual.data/201.rlrdata")
print(my_data)

all_data = {}
for location_number in range(202,204):
    location_string = str(location_number)
    my_data = get_sealevel_data_from_url('http://www.psmsl.org/data/obtaining/rlr.annual.data/' + location_string + '.rlrdata')
    all_data[location_string] = my_data
print(all_data)

x_202 = all_data['202'][0]
y_202 = all_data['202'][1]
x_203 = all_data['203'][0]
y_203 = all_data['203'][1]

import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np  # for np.nan values
array_x_202 = np.array([x_202]).T  # note - data has to be wrapped in a second list to transpose
array_y_202 = np.asarray(y_202)
array_x_203 = np.array([x_203]).T  # note - data has to be wrapped in a second list to transpose
array_y_203 = np.asarray(y_203)

print(type(array_x_202))
print(array_x_202.shape)
print(type(array_y_202))
print(array_y_202.shape)

regr_202 = linear_model.LinearRegression()
# Train the model using the training sets
regr_202.fit(array_x_202, array_y_202)

regr_203 = linear_model.LinearRegression()
regr_203.fit(array_x_203, array_y_203)

# The coefficients
print('Coefficients: \n', regr_202.coef_)

# The mean squared error
mean_squared_error = np.mean((regr_202.predict(array_x_202) - array_y_202) ** 2)
print("Mean squared error: {:.2f}".format(mean_squared_error))

# Plot x and y values
plt.scatter(array_x_202, array_y_202, color='black')
plt.plot(array_x_202, regr_202.predict(array_x_202), color='black', linewidth=3)
plt.scatter(array_x_203, array_y_203, color='blue')
plt.plot(array_x_203, regr_203.predict(array_x_203), color='blue', linewidth=3)
print('--')
print('Estimated sea level at Newlyn in 2050 is {:.2f} mm.'.format(regr_202.predict(2050)[0]))
print('--')
# Add ticks on the axes
# plt.xticks()  # range(min(array_x), max(array_x)+1, 10))  # np.arange(min(array_x), max(array_x)+1, 10)
# plt.yticks()

# Display the plot
plt.show()

# find station 203 here: http://www.psmsl.org/data/obtaining/
# reason for drops in some places
# http://io9.gizmodo.com/why-are-sea-levels-dropping-in-places-closest-to-the-me-1684599241

