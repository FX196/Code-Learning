#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    r = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    primes = [x for x in primes if x <= n]
    for prime in primes:
        r.append(prime)
        while r[-1] * prime < n:
            r[-1] *= prime
    res = 1
    for num in r:
        res *= num
    print(res)
