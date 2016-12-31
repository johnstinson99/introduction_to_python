# https://onlinecourses.science.psu.edu/stat501/sites/onlinecourses.science.psu.edu.stat501/files/data/bluegills.txt
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

x_age = []
y_length = []
with open('bluegill_fish_lengths.txt', mode='r') as a_file:
    my_reader = csv.DictReader(a_file, delimiter='\t')
    # for a_dict in my_reader:
    #     print(a_dict)
    for a_dict in my_reader:
        x_age.append(int(a_dict['age']))
        y_length.append(int(a_dict['length']))

print(x_age)
print(y_length)

# x_age_array = np.array(x_age)
# y_length_array = np.array(y_length)
list_of_power_colour_tuples = [(2, 'blue'),
                               (3, 'black'),
                               (4, 'red'),
                               (5, 'yellow')]

polyfit = np.poly1d(np.polyfit(x_age, y_length, 2))
polyfit_tuple_list = [(degree, colour, np.poly1d(np.polyfit(x_age, y_length, degree)))
                      for degree, colour in list_of_power_colour_tuples]

print(polyfit)
print(type(polyfit))
print(polyfit(3))
print(polyfit.coeffs)
print(polyfit.order)
print(polyfit.deriv())
print(polyfit.integ())
deriv = polyfit.deriv(m=1)
integ = polyfit.integ()
# label axes
fig = plt.figure()
subplot = fig.add_subplot(111)
subplot.set_xlabel('fish age')
subplot.set_ylabel('fish length')
subplot.set_title('lengths of bluegill fish by age')
plt.scatter(x_age, y_length,  color='black', label='fish length')

unique_x_values = range(min(x_age) - 2, max(x_age) + 3)
unique_x_values = np.linspace(min(x_age), max(x_age), 100)
print(type(unique_x_values))
# plt.plot(unique_x_values, polyfit(unique_x_values), color='blue', label='polynomial regression fit')  # plt.plot(list(set(x_age)), z(list(set(x_age))), color='blue')
for my_degree, my_colour, my_polyfit_equation in polyfit_tuple_list:
    plt.plot(unique_x_values,
             my_polyfit_equation(unique_x_values),
             color=my_colour,
             label='polynomial fit degree ' + str(my_degree))
plt.plot(unique_x_values, deriv(unique_x_values), color='red', label='first derivative')  # plt.plot(list(set(x_age)), z(list(set(x_age))), color='blue')
# plt.plot(unique_x_values, integ(unique_x_values), color='black')  # plt.plot(list(set(x_age)), z(list(set(x_age))), color='blue')

subplot.legend(bbox_to_anchor=(0.6, .25))
plt.show()
