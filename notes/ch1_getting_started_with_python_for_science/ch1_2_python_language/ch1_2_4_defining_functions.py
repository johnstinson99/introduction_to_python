from math import pi

def test():
    print('in test function')

test()


def circle_area(radius):
    """
    Work out area of a circle
    :param radius: the radius
    :return: area of circle
    """

    return pi*radius**2


print(circle_area(radius=4))
print(type(circle_area))
print('help = ')
help(circle_area)

my_func = circle_area
print("my_func = ", my_func)
a = my_func
print("a = ", a)

print(a(4))

x = 3
print(eval("x + 1"))

import math
new_list = list(map(math.sqrt, range(1, 10)))
print(new_list)

class my_class():
    def __repr__(self):
        return 'Wahaha!'

a = my_class
print(str(a))

# fibonnaci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fib_series(n):
    fib_list = [0, 1]
    for i in range(0, n-2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

print(fib_series(10))

def fib_number(n):
    if n < 2:
        return n
    else:
        return fib_number(n-1) + fib_number(n-2)

for i in range(10):
    print(fib_number(i))

def pascals_triangle(n):
    result = [[1], [1,1]]
    for current_element_number in range(2, n):
        prior = [0] + result[current_element_number - 1] + [0]
        new_result = []
        for j in range(0, len(prior)-1):
            new_result.append(prior[j]+prior[j + 1])
        result.append(new_result)
    return result

print(pascals_triangle(20))


def pp_tri(n):
    result = [[1]]
    for row_number in range(1, n):
        prior_row_shifted_left = result[-1] + [0]
        prior_row_shifted_right = [0] + result[-1]
        pairs = list(zip(prior_row_shifted_left, prior_row_shifted_right))
        # print(list(pairs))
        next_row = [sum(my_pair) for my_pair in pairs]
        # print(next_row)
        result.append(next_row)
    return result

print('pp_tri')
print(pp_tri(6))

def pas_tri(n):
    rows = [[1]]
    for i in range(1, n+1):
        rows.append([1] +
                    [sum(pair) for pair in zip(rows[-1], rows[-1][1:])] +
                    [1])
    return rows
print('pas_tri')
print(pas_tri(10))


def quicksort(my_list):
    less = []
    greater = []
    if len(my_list) <= 1:
        return my_list
    pivot = my_list.pop()  # takes last item from list
    for x in my_list:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    result = quicksort(less) + [pivot] + quicksort(greater)
    return result

print(quicksort([3, 2, 5, 1, 8]))

