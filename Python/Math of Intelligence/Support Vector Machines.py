import numpy as np
from matplotlib import pyplot as plt

X = np.array([
    [-2, 4, -1],
    [4, 1, -1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],
])

Y = np.array([-1, -1, 1, 1, 1])

"""
for d, sample in enumerate(X):
    # Plot the negative samples (the first 2)
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    # Plot the positive samples (the last 3)
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)
plt.show()
"""

# initialize weights
w = np.zeros(len(X[0]))

epochs = 100000
errors = []
eta = 1
for epoch in range(1, epochs):
    error = 0
    for i in range(len(X)):
        if (Y[i] * np.dot(X[i], w)) < 1:
            w = w - eta * (2 * (1 / epoch) * w + (-X[i] * Y[i]))
            error = 1
        else:
            w = w - eta * 2 * (1 / epoch) * w
    errors.append(error)

"""
plt.plot(errors, '|')
plt.ylim(0.5,1.5)
plt.axes().set_yticklabels([])
plt.xlabel('Epoch')
plt.ylabel('Misclassified')
"""

for d, sample in enumerate(X):
    # Plot the negative samples
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    # Plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)

# Add our test samples
plt.scatter(2, 2, s=120, marker='_', linewidths=2, color='yellow')
plt.scatter(4, 3, s=120, marker='+', linewidths=2, color='blue')

# Print the hyperplane calculated by svm_sgd()
x2 = [w[0], w[1], -w[1], w[0]]
x3 = [w[0], w[1], w[1], -w[0]]

x2x3 = np.array([x2, x3])
X, Y, U, V = zip(*x2x3)
ax = plt.gca()
ax.quiver(X, Y, U, V, scale=1, color='blue')

plt.show()
