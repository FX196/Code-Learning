#!/bin/python3


def product(s):
    res = 1
    for n in s:
        res *= int(n)
    return res


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input()
    max = 0
    for i in range(len(num) - k):
        prod = product(num[i:i + k])
        if prod > max:
            max = prod
    print(max)
