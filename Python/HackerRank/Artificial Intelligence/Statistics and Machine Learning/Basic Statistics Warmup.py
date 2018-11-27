from statistics import *
n = input()
x = input().split(" ")
x = list(map(lambda s: float(s), x))
mean = float(sum(x))/len(x)
x.sort()
median = median(x)
mode = mode(x)
std = stdev(x)
low = mean - 1.96*std
hi = mean + 1.96*std
print("%.1f" % mean)
print("%.1f" % median)
print("%d" % mode)
print("%.1f" % std)
print("%.1f %.1f" % (low, hi))
