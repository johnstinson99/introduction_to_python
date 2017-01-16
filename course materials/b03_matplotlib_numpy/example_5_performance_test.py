import time
import math
import numpy as np
import matplotlib

def time_a_function(my_func: __name__, my_param: int):
    """
    Times how long it takes to execute a function
    Time in ms, accurate to approximately the nearest millisecond.
    :param my_func: name of function to be timed
    :param my_param: parameter to be passed to the function
    """
    start_time_list = time.time()
    my_func(my_param)
    time_diff_ms = (time.time() - start_time_list)*1000
    # print(my_func.__name__, 'iterations =', my_param, 'time =', time_diff_ms, 'ms')
    return time_diff_ms


def process_list(my_iterations: int):
    """
    Take the sin() of a list of floats
    :param my_iterations: number of iterations
    """
    x_list = [j / 100 for j in range(my_iterations)]
    y_list = [math.sin(x) for x in x_list]
    # print(y_list[-1])


def process_np(my_iterations: int):
    """
    Take the sin() of a numpy array of floats
    :param my_iterations: number of iterations
    """
    x_array = np.arange(0, 20, 20 / my_iterations)
    y_array = np.sin(x_array)
    # print(y_array[-1])


# Time list vs numpy approaches - see chart.
iterations_x_positions = []
iterations_x_labels = []
times_for_process_list_method_y1 = []
times_for_process_np_method_y2 = []
for i in range(0, 7):  # 3 to 8 works
    print(i)
    iterations = 10**i
    iterations_x_positions.append(i)
    iterations_x_labels.append(iterations)
    times_for_process_list_method_y1.append(time_a_function(process_list, iterations))
    times_for_process_np_method_y2.append(time_a_function(process_np, iterations))

x_array = np.array(iterations_x_positions)
import matplotlib.pyplot as plt

bar_width = 0.35  # 1 distance between bars is 1 unit on x axis

plt.bar(x_array - bar_width/2,
        np.array(times_for_process_list_method_y1),
        width=bar_width,
        align='center',
        log=True,
        color='red',
        label='List Method')

plt.bar(x_array + bar_width/2,
        np.array(times_for_process_np_method_y2),
        width=bar_width,
        align='center',
        log=True,
        label='NumPy Array Method')

plt.ylabel('Time, ms')
plt.xlabel('Iterations')
plt.xticks(iterations_x_positions, iterations_x_labels)
plt.legend(loc='upper center')

plt.show()


