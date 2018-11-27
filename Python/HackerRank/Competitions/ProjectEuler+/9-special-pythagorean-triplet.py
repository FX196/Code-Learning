#!/bin/python3


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    maximum = -1
    for a in range(n - 1, 0, -1):
        b = (((2 * a) - n) * n) / (2 * (a - n))
        c = n - a - b
        if b == int(b) and c == int(c) and a != b and b != c and a != c:
            if a * b * c > maximum:
                maximum = a * b * c
    print(int(maximum))
