import matplotlib.pyplot as plt

x_list = [1, 2, 3, 4, 5]
y1_list = [1, 2, 3, 4, 5]
y2_list = [2, 3, 4, 5, 6]
plt.plot(x_list, y1_list, color='r', linestyle='', marker='o')
plt.plot(x_list, y2_list, color='b', linestyle='-', linewidth=1, marker='o')

plt.xticks(x_list, ['alpha', 'bravo', 'charlie', 'delta', 'echo'], rotation='vertical')

# Extend to cover the steps below.

# Leave margins between axes and the lines/dots
# plt.margins(.2)

# Tweak spacing to prevent clipping of tick-labels
# plt.subplots_adjust(bottom=0.15)

# Add yticks too
# plt.yticks(x_list, ['a', 'b', 'c', 'd', 'e'], rotation='vertical')

plt.show()
