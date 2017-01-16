import matplotlib.pyplot as plt

x_list = [1, 2, 3, 4, 5]
y1_list = [1, 2, 3, 4, 5]
y2_list = [2, 3, 4, 5, 6]
plt.plot(x_list, y1_list, color='r', linestyle='', marker='o', label='line 1')
plt.plot(x_list, y2_list, color='b', linestyle='-', linewidth=1, marker='o', label='line 2')

plt.xticks(x_list, ['alpha', 'bravo', 'charlie', 'delta', 'echo'], rotation='vertical', fontsize='x-large')
plt.margins(.2)
plt.subplots_adjust(bottom=0.15)
plt.yticks(range(1,7), range(1,7), fontsize='x-large')

plt.legend(loc='upper center', shadow=True, fontsize='x-large')

plt.show()
