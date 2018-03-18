#!/bin/python3

t = int(input())
while t > 0:
    n = int(input())
    j = n * (n + 1) * (2 * n + 1) // 6
    m = n * (n + 1) // 2
    m = m * m
    print(m - j)
    t -= 1
