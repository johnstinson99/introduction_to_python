import matplotlib.pyplot as plt

x_list = [1, 2, 3, 4, 5]
y_list = [1, 2, 3, 4, 5]
plt.plot(x_list, y_list, color='r', linestyle='', marker='o')

plt.show()

# Note - can abbreviate to this form, but less readable: plt.plot(x, y, 'r-d')
# See quick reference card for full list of parameters