import random
import numpy

# random.seed(3)  # make it reproducible for testing
i = random.choice(range(1, 7))  # could be a choice of any list eg a list of strings.
i = random.randrange(1, 7)  # allows steps, doesn't include the end point
# i = random.randint(1, 6)  # includes both end points

print(i)
my_list = [random.randrange(1, 7) for i in range(2)]
print (my_list)

# numpy gives us more flexibility of specifying how many random numbers we want, and with what probabilities.
# j = numpy.random.choice(range(1, 7), size=2, p=[0.02, 0.03,0.05, 0.1, 0.3, 0.5])
# print(j)
# print(type(j))

