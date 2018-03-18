#!/bin/python3

l = [2, 3]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while len(l) < n:
        i = l[-1] + 2
        prime = False
        while not prime:
            j = 0
            while j < len(l) and i % l[j] != 0 and l[j] < i ** 0.5 + 2:
                j += 1
            if j < len(l) and i % l[j] == 0:
                i += 2
            else:
                prime = True
                l.append(i)
    else:
        print(l[n - 1])
