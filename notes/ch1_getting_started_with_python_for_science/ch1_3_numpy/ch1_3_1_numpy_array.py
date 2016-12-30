import numpy as np

numpy_array = np.array([1,2,3,4])
print(numpy_array)
# #
# my_list = range(1000)
# %timeit [i**2 for i in my_list]
# #

# a = np.arange(1000)
# %timeit a**2

# from time import time
# import time
# print(time.time())
#
# def square_a_list(iterations):
#     result = [(i/100)**2 for i in range(iterations)]
#     print(result[:10], result[-1000:])
#     return result
#
# def square_a_numpy_array(iterations):
#     a = np.arange(iterations)
#     result = (a/100)**2
#     print(result[:10], result[-1000:])
#     return result
#
#
# def time_it(a_function, iterations):  # note - only measures to nearest 16ms!
#     a = time.time()
#     result = a_function(iterations)  # a_function(10000001)
#     # print(result[:10], result[-5:])
#     b = time.time()
#     print('a, b = ', a, b)
#     time_diff_milliseconds = (b - a) * 1e3
#     return time_diff_milliseconds
#     print('Time difference for {} function is {:.2f} us'.format(a_function.__name__, time_diff_milliseconds, 0))
#
# time_it(square_a_list, 1000)
# time_it(square_a_numpy_array, 1000)
#
# iterations = [10**a for a in range(8)]
# print(iterations)
# results = [(i, time_it(square_a_list, i), time_it(square_a_numpy_array, i)) for i in iterations]
# with open('results.txt', 'w') as my_file:
#     for a, b, c in results:
#         my_file.write(str(a) + '\t' + str(b) + '\t' + str(c) + '\n')

# print(results)
# help(np.array)
# my_matrix = np.mat('1, 2; 3 4')
# print(my_matrix)

my_array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
print(my_array_2d)
print(my_array_2d.shape)
print(my_array_2d.size)

my_array_3d = np.array([[[1, 2],[3, 4]],
                       [[5, 6], [7, 8]]])
print(my_array_3d)
print(my_array_3d.shape)
print(my_array_3d.size)

list1 = [1, 2, 3]
list2 = [4, 5 ,6]
array_made_from_list_of_lists = np.array([list1, list2])
print(array_made_from_list_of_lists)

array_made_from_list_of_ranges = np.array([range(1, 5), range(11, 15)])
print(array_made_from_list_of_ranges)

array_made_from_list_of_ranges_2 = np.array([range(0, 10, 2), range(20, 10, -2)])
print(array_made_from_list_of_ranges_2)

string_array = np.array([['ab', 'b'], ['c', 'd']])
print(string_array)

# =========

my_array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])


def print_array(an_array):
    print(an_array)
    print(an_array.shape)
    print(an_array.size)
    print(len(an_array))
    print(an_array.ndim)

print_array(my_array_2d)
print_array(my_array_3d)

a = np.arange(10)
print(a)
a = np.arange(0, 10, 2)
print(a)
a = np.arange(10, 0, -2)
print(a)
a = np.linspace(1,100, 7) # spaces evenly by the final parameter
print(a)
a = np.linspace(1,100, 7, endpoint=False) # spaces evenly by the final parameter
print(a)


# Common arrays
a = np.ones([2,2,3])
print(a)
a = np.zeros([3,4])
print(a)
a = np.eye(3)
print(a)
a = np.diag([1,2,3,4])
b = np.diag(range(1,5))
c = np.diag(np.arange(1,5))
print(a,'\n', b, '\n', c)

# Random
np.random.seed(1234)  # always returns the same numbers. Useful for testing.
a = np.random.rand(4)  # evenly distributed between 0 and 1
a = np.random.rand(2,2)  # evenly distributed between 0 and 1
a = np.random.rand(2,2,2)  # evenly distributed between 0 and 1
print(a)
a = np.random.randn(10)  # normal distribution around 0
a = np.random.randn(3,3,3)  # normal distribution around 0
print(a)

# data types
c = np.array([1, 2, 3], dtype=float)
print(c)
print(c.dtype)
d = np.array([1+2j, 3+4j, 5+6*1j])
print(d.dtype)
e = np.array([True, False, False, True])
print(e.dtype)
e2 = np.ones(5, dtype=bool)
print(e2)
print(e2.dtype)
f = np.array(['Bonjour', 'Hello', 'Hallo',])
print(f.dtype)

#
import matplotlib.pyplot
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
# matplotlib.pyplot.plot(x, y)
# matplotlib.pyplot.plot(x, y, 'o')
# # matplotlib.pyplot.show()

image = np.random.rand(1000, 1000)
# matplotlib.pyplot.imshow(image, cmap=matplotlib.pyplot.cm.hot)
# matplotlib.pyplot.imshow(image, cmap=matplotlib.pyplot.cm.gray)
# matplotlib.pyplot.colorbar()
# matplotlib.pyplot.show()

# import math
# t = np.arange(0.0, 1.0, 0.01)
# s_sin = np.sin(2*math.pi*t)
# s_cos = np.cos(2*math.pi*t)
# print(s_cos.dtype)
# print(t)
# print(s_cos)
# matplotlib.pyplot.plot(t, s_sin, color='blue', lw=2)
# matplotlib.pyplot.plot(t, s_cos, color='green', lw=2)
# # line, = ax.plot(t, s, color='blue', lw=2)
# matplotlib.pyplot.show()

a = np.arange(10)
print(a[0])
print(a[-3])
print(a[10:0:-2])
print(a[::-1])

a = np.diag(np.arange(3))
print(a)
print(a[1,1])  #row,column
a[1,2] = 9  #row,column
print(a)

a = np.array([range(0,6),
              range(10,16),
              range(20,26),
              range(30,36),
              range(40,46),
              range(50,56)])
print(a)
print(a[3,4])       # single number 34 at 3rd row and 4th column
print(a[0,3:5])     # row 0, columns 3:5
print(a[2:4,2:4])   # rows 2:4, columns 2:4
print(a[4,0:6])     # row 4, all columns
print(a[4,])        # same as above. You don't need to specify both dimensions
print(a[::2, ::2])  # every other number. Useful in cutting down matrix resolution

# assigning to slices.
a[::2, ::2] = '0'
print(a)
nought_to_nine = np.arange(10)
print(nought_to_nine)
nought_to_nine[5:] = 0
print(nought_to_nine)
nought_to_nine[5:] = np.arange(5,0,-1)
print(nought_to_nine)
print(np.arange(5, 0, -1))
print(np.arange(5)[::-1])

# creating a 6*6 array
# first create a long thin array
print(np.arange(0, 51, 10)[:, np.newaxis])
# now add it to a horizontal array
print(np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis])
#

# print(a)

c = np.array([1., 2., 3.], dtype=int)
print(c)

a = np.ones([4,4], dtype=int)
a[2,3] = 2
a[3,1] = 6
print(a)


a = np.diag(np.arange(2., 7.), k=-1)  # note can't use range here as range doesn't accept floats.
print(a)

help(np.tile)

a = np.array([[1,2],[3,4]])
print(a)
tiled = np.tile(a, [4,4])
print(tiled)

a = np.arange(10)
print(a)
b = a[:5]
print(b)
b[4] = 99
print(b)
print(a)

# To avoid this behaviour use a.copy()

# is_prime = np.ones(100, dtype=bool)
# # print(is_prime)
# for i in range(2,10):
#     is_prime[2*i::i] = False
# # print(is_prime)
# primes = np.nonzero(is_prime)
# print(primes)

is_prime = np.ones(100, dtype=bool)
# print(is_prime)
is_prime[0:2] = False
for i in range(2,10):
    is_prime[i*i::i] = False
# print(is_prime)
primes = np.nonzero(is_prime)
print(primes)

# FANCY INDEXING USING MASKS
a = np.array([10,  3,  8,  0, 19, 10, 11,  9, 10,  6,  0, 20, 12,  7, 14])
divisible_by_3_mask_array = a % 3 == 0
print(divisible_by_3_mask_array)
b = a[divisible_by_3_mask_array]
print(b)

# FANCY INDEXING USING MASK TO ASSIGN VALUE
a[divisible_by_3_mask_array] = 999
print(a)

# FANCY INDEXING WITH ARRAY OF INTEGERS
a = np.arange(0,100,10)
print(a)
print(a[[0,5,5,6]])
a[[0,5,6]] = 99
print(a)

# FANCY INDEXING: INDEXING FLAT ARRAY WITH MULTIDIMENSIONAL ARRAY
a = np.arange(0,100,10)
print(a)
numeric_index_array = np.array([[2,3], [6,7]])
print(numeric_index_array)
b = a[numeric_index_array]
print(b)

# FANCY INDEXING EXAMPLES
b = np.arange(0, 6)
c = np.array([[0],[10],[20],[30],[40],[50]])
a = b + c
print(a)

# row 0, column 1
# row 1, column 2
# etc
print(a[(0,1,2,3,4),(1,2,3,4,5)])
print(a[[0,1,2,3,4],[1,2,3,4,5]])  # works with list, tuple or range
print(a[range(0,5), range(1,6)])

print(a[3:, [0, 2, 5]])

mask = np.array([1, 0, 1, 0, 0, 1], dtype=bool)
print(a[mask, 2])

# EXERCISE - set top right 2*2 square of numbers to zero.
print(a[0:2, 4:6])
a[0:2, 4:6] = 0
print(a)

