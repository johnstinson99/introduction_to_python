import functools
import math
from math import factorial, pow

# if elif else
for i in range(0, 20, 2):
    print(i)
for my_char in ['a', 'b', 'c']:
    print(my_char)

a = 0
while a < 10:
    print(a)
    a += 3
    if a > 6:
        break

d = {'a': 1, 'b': 1.2, 'c': 1j}
for key, val in sorted(d.items()):  # Sorts on first element of the tuple.
    print('Key: %s has value: %s' % (key, val))

my_list = [4 * i ** 2 / (4 * i ** 2 - 1) for i in range(1, 1000)]

print(my_list[:10])
result = 1
for item in my_list:
    result *= item
print('result = ')
print(result * 2)

def multiply(x,y):
    return x*y

result2 = functools.reduce(multiply, my_list)
print('result2 = ')
print(result2 * 2)

# Newtons formula for pi version 1
# series = [math.factorial(2.*n) /
#           (math.pow(2., 4.*n + 2.) * math.factorial(n)**2. * (2.*n - 1.) * (2.*n + 3.)) for n in range(0, 21)]
# result = 24*(math.sqrt(3)/32 - sum(series))
# print(result)

series = [math.factorial(2*n)/
          (math.pow(2, 4*n + 1) * math.factorial(n)**2 * (2*n + 1)) for n in range(0,20)]
print('newton result = ', 6*sum(series))

# Newtons formula for pi
series = [math.factorial(2. * n) /
          (math.pow(2., 4. * n + 2.) * math.factorial(n) ** 2. * (2. * n - 1.) * (2. * n + 3.)) for n in range(0, 21)]
result = 24 * (math.sqrt(3) / 32 - sum(series))
print(result)
# Newton 2
series = [math.pow(2, k)* math.factorial(k)**2 /
          math.factorial(2*k + 1) for k in range(0,50)]
print(2* sum(series))

# Chudnovsky
def chud(k_max):
    chud_series = [(math.pow(-1, k) * math.factorial(6*k) * (545140134 * k + 13591409))/
                   (math.factorial(3*k) * math.pow(math.factorial(k), 3)) * math.pow(640320, 3*k + 3/2)
                   for k in range(0, k_max)]
    print(chud_series[:10])
    res = 2 * sum(series)
    return res
for k_max in range(1,10):
    print('Chudnovsky = ', k_max, ' = ', chud(k_max))

def chud2(n_max):
    chud_series = [((pow(-1, n)*factorial(6*n))/(factorial(3*n)*pow(factorial(n), 3))) *
                   ((13591409 + 545140134 * n)/math.pow(math.pow(640320, 3), n+.5))
                   for n in range(0,10)]
    return(1/(12*sum(chud_series)))

for n_max in range(1,5):
    print('Chudnovsky2 = ', n_max, ' = ', chud2(n_max))

new_list = [n*2 for n in range(0, 10)]
my_sum = sum(new_list)
# sigma n = 0, 9  n*2
print(new_list)
