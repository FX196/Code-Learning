#!/bin/python3


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while n % 2 == 0:
        n //= 2
    if n <= 2:
        print(2)
        continue
    else:
        i = 3
        while i < n ** 0.5 + 2:
            if n % i == 0:
                n //= i
                i = 3
            else:
                i += 2
        if n > 2:
            print(n)
        else:
            print(i)
