import matplotlib.pyplot as plt

x_list = [1, 2, 3, 4, 5]
y1_list = [1, 2, 3, 4, 5]
y2_list = [2, 3, 4, 5, 6]
plt.plot(x_list, y1_list, color='r', linestyle='', marker='o')
plt.plot(x_list, y2_list, color='b', linestyle='-', linewidth=1, marker='o')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Title')

plt.show()
