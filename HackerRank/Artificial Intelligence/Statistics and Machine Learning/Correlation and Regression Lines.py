import numpy as np
from numpy.linalg import *

x = np.array([[15, 12, 8, 8, 7, 7, 7, 6, 5, 3]])
y = np.array([[10, 25, 17, 11, 13, 17, 20, 13, 9, 15]])
x = x.transpose()
y = y.transpose()

# 1 correlation coefficient
x_mean = np.mean(x)
y_mean = np.mean(y)
a = 0.0
b = 0.0
c = 0.0
for i in range(len(x)):
    a += (x[i] - x_mean) * (y[i] - y_mean)
    b += (x[i] - x_mean) ** 2
    c += (y[i] - y_mean) ** 2
r = a / ((b ** 0.5) * (c ** 0.5))
print(r)

# 2 regression line slope
A = np.vstack([x.T, np.ones(len(x))]).T
m, c = lstsq(A, y, rcond=None)[0]
print(m, c)

# 3 predict score
score = 10 * m + c
print(score)

# 4
