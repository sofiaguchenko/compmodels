import matplotlib.pyplot as plt
from random import random
import math
import scipy.stats

n = 10000
gamma = 100
x = []
for i in range(n):
    ksi = random()
    x.append(- math.log(ksi) / gamma)

h = (max(x) - min(x)) / 20
intervals = []
for i in range(21):
    intervals.append(min(x) + h * i)

# the number of hits of the generated numbers in the intervals
y = [0 for i in range(20)]
for i in range(len(x)):
    for j in range(len(y)):
        if intervals[j] <= x[i] <= intervals[j + 1]:
            y[j] += 1

        # checking for compliance with the exponential law of distribution
arithmetic_mean = sum(x) / n
l = 1 / arithmetic_mean
p = []
for i in range(20):
    p.append(n * (math.exp(- l * intervals[i]) - math.exp(- l * intervals[i + 1])))
chi2 = sum([(y[i] - p[i]) ** 2 / p[i] for i in range(len(y))])
chi2_tabular = scipy.stats.chi2.ppf(q=0.99, df=19)

print('The significance level α=0.05 and the number of degrees of freedom 19')
print('The tabular value of the criterion: ', chi2_tabular)
print('The calculated value of the criterion: ', chi2)

if chi2 <= chi2_tabular:
    print('With a confidence probability of 0.99 the random variable is distributed '
          'according to the exponential distribution law.')
else:
    print('With a confidence probability of 0.99 the random variable is not distributed according to the exponential distribution law.')

    plt.bar(intervals[0:20], y, width=h)
    plt.show()