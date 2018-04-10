#!/bin/python3


def factors(x):
    res = []
    for i in range(100, 1000):
        if x % i == 0:
            res.append(i)
    return res


def is_palindrome(x):
    return str(x) == str(x)[::-1]


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n <= 101101:
        print(99999)
        continue
    else:
        n = ((n - 1) // 11) * 11
        found = False
        while not found:
            fac = factors(n)
            for i in fac:
                if n // i in fac:
                    if is_palindrome(n):
                        print(n)
                        found = True
                        break
            n -= 11
