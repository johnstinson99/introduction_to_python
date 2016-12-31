a = 1.5 + 0.5j
b = 2 + 3j
c = a+b 
print(c)
print(type(c))

print(type(1))
print(type(2.5))
print(type('Hello'))
print(type(True))

# type conversion
print(float(1))

# integer division
print(3//2)
print(round(1.5))

print(type([1,2,3]))
print(type((1,2)))
print(type({1:'a', 2:'b'}))
my_list = [1,2,3,4,5,6,7,8]
print(my_list[4:8:2])  # [5,7]  [start:stop:stride]
print(my_list[::2])  # [1, 3, 5, 7]
my_list[2:4] = ['a', 'b'] # lists are mutable
print(my_list)  # [1, 2, 'a', 'b', 5, 6, 7, 8]

a = 20.5
b = 30.2
print('hello there apples = ', format(a, "00000"), ', pears = {b}', format("0.0"), format("0"))

print("The sum of 1 + 2 is {} or {}".format(1+2, 'hi'))

print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centre aligned'))
print('{:*^30}'.format(' centre aligned ')) # nice

print('{:,}'.format(1234567890))

points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))

import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

