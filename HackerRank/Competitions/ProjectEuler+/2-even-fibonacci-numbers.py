#!/bin/python3


def even_fib(x):
    l = [0, 2]
    while l[-1] <= x:
        l.append(l[-1] * 4 + l[-2])
    return sum(l[:-1])


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(even_fib(n))
