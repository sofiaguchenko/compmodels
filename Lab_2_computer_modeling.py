import numpy as np
import pylab


def function(x, b):
    f = 0
    for i in range(len(b)):
        f += b[i] / (x ** i)
    return f


Xgiven = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]
Ygiven = [14.0, 18.222, 18.0, 17.216, 16.444, 15.778, 15.219, 14.749, 14.352,
          14.014, 13.722, 13.469, 13.248, 13.052, 12.879, 12.724]

bestB = []
minCriterion = 100
for n in range(15):
    X = np.ones((len(Xgiven), n + 1))
    for i in range(1, n + 1):
        for j in range(len(Xgiven)):
            X[j, i] = 1 / (Xgiven[j] ** i)
    Y = np.array([[Ygiven[i]] for i in range(len(Xgiven))])
    transposedX = X.transpose()
    reversedXtX = np.linalg.inv(transposedX.dot(X))
    B = (reversedXtX.dot(transposedX)).dot(Y)
    criterion = sum([(function(Xgiven[i], B) - Ygiven[i]) ** 2 for i in
                     range(len(Xgiven))])
    if criterion < minCriterion:
        minCriterion = criterion
        bestB = B

print('Least squares criterion =', float(minCriterion))
print('Calculated the best bі:', [round(float(bestB[i]), 6) for i in
                                  range(len(bestB))])
print('Calculated y:', [round((float(function(Xgiven[i], bestB))), 3) for i in
                        range(len(Xgiven))])
print('Given y:', Ygiven)

pylab.subplot(1, 2, 1)
pylab.plot(Xgiven, Ygiven)
pylab.title('Given')

pylab.subplot(1, 2, 2)
pylab.plot(Xgiven, [function(Xgiven[i], bestB) for i in range(len(Xgiven))])
pylab.title('Calculated')

pylab.show()