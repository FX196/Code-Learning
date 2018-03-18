import numpy as np

f = open('Laptop Battery Life-trainingdata', 'r')

data = f.read()
lines = data.splitlines()
x = []
y = []
for line in lines:
    line = line.split(',')
    x.append(float(line[0]))
    y.append(float(line[1]))
# plt.plot(x, y, 'ro')
# plt.show()

x_reg = []
y_reg = []
for i in range(len(x)):
    if y[i] != 8.00:
        x_reg.append(x[i])
        y_reg.append(y[i])
x_reg = np.array(x_reg)
y_reg = np.array(y_reg)

a = np.vstack((x_reg.T, np.ones(len(x_reg)))).T
m, c = np.linalg.lstsq(a, y_reg, rcond=None)[0]
print(m, c)  # 2, 0

n = float(input())
print("%.2f" % min(n * 2, 8.00))
