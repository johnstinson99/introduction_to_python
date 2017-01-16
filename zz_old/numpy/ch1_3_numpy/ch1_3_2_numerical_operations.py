import numpy as np

# scalar arithmetic with arrays
a = np.arange(0, 5)
print(a)
print(a + 1)
print(2**a)

# adding or subtracting arrays of the same dimensions
b = np.ones(5, dtype=int) + 1
print(b)
print(a-b)

# ARRAY MULTIPLICATION IS NOT MATRIX MULTIPLICATION
c = np.ones([3,3], dtype=int)
print(c)
print(c*c)
# returns 3*3 array of ones

# USE DOT PRODUCT FOR MATRIX MULTIPLICATION
print(c.dot(c))
# returns 3*3 array of 3s


def sum_array(size):
    a = np.arange(size)
    b = a + 1

def sum_list(size):
    a = range(size)
    b = [i + 1 for i in a]

def time_it(a_function, iterations):  # note - only measures to nearest 16ms!
    import time
    a = time.time()
    a_function(iterations)  # a_function(10000001)
    b = time.time()
    print('a, b = ', a, b)
    time_diff_milliseconds = (b - a) * 1e3
    print('Time difference for {} function is {:.2f} ms'.format(a_function.__name__, time_diff_milliseconds, 0))
    return time_diff_milliseconds

# a = time_it(sum_array, 10000000)
# b = time_it(sum_list, 10000000)
# print(b/a)

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b)
print(a > b)

# comparison
a = np.array([1,2,3,4])
b = np.array([2,2,3,4])
c = np.array([1,2,3,4])
print(np.array_equal(a, b))
print(np.array_equal(a, c))

# np.allclose()  # arrays the same within a certain tolerance
# np.triu()  # upper triangle of array
# np.tril()  # lower triangle of array

a = [[0,1,2],[10,11,12],[20,21,22]]
print(a)
print(np.triu(a))
print(np.tril(a))
