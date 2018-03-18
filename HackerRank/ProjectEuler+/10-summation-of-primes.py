#!/bin/python3


l = [True] * (10 ** 6 + 1)
for i in range(2, 10 ** 6 + 1):
    if not l[i]:
        continue
    else:
        j = 2
        while i * j <= 10 ** 6:
            l[i * j] = False
            j += 1
l2 = [0] * (10 ** 6 + 1)
sum = 0
for i in range(2, 10 ** 6 + 1):
    if l[i]:
        sum += i
    l2[i] = sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(l2[n])

"""
used Sieve of Eratosthenes algorithm
not enough to recalculate sum for each input
pre-calculate for all n < 1000000
and directly print from stored array
"""
