"""
Demo of the histogram (hist) function with a few features.

In addition to the basic histogram, this demo shows a few optional features:

    * Setting the number of data bins
    * The ``normed`` flag, which normalizes bin heights so that the integral of
      the histogram is 1. The resulting histogram is a probability density.
    * Setting the face color of the bars
    * Setting the opacity (alpha value).

"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random

print('-- random module --')
# returns a single value from a normal distribution
print(random.random())  # no arguments. Random number between zero and one
print(random.normalvariate(100, 15))  # mu, sigma
print(random.gauss(100, 15))  # mu, sigma  # slightly faster than normalvariate
print(random.lognormvariate(100, 15))  # mu, sigma
print(random.expovariate(1))  # argument lambda
print(random.betavariate(2, 3))  # arguments alpha, beta
print()
print('-- numpy module --')
print(np.random.random())  # single random number
print(np.random.rand(10))  # array of 10 evenly distributed numbers
print(np.random.logistic(5, 2, 10)) # loc, scale, size
# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution

# randn is random NORMAL DISTRIBUTION. It returns a numpy array of floats.
# mean = 0, standard deviation = 1
# standard_normal does the same.
# x = np.random.standard_normal(10000)
x = mu + sigma * np.random.randn(10000)

# Logisic distribution
x = np.random.logistic(30, 10, 10000)

x = np.random.exponential(10, 10000)

x = np.random.lognormal(30, 10, 10000)
print(type(x))
print(x)

num_bins = 50
# the histogram of the data
# plt.hist groups the data into bins.
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5, log=True)
# add a 'best fit' line
# y = mlab.normpdf(bins, mu, sigma)
# plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.savefig('my_graph', frameon=False)
plt.show()
