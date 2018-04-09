#!/bin/python3

def getWaysMem(n, c, ind, d):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif ind < 0:
        return 0
    elif n in d.keys() and ind in d[n].keys():
        return d[n][ind]
    else:
        if not n in d.keys():
            d[n] = {}
        d[n][ind] = getWaysMem(n, c, ind - 1, d) + getWaysMem(n - c[ind], c, ind, d)
        return d[n][ind]


def getWays(n, c):
    d = {}
    return getWaysMem(n, c, len(c) - 1, d)

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
