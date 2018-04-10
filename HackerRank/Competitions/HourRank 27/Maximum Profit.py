#!/bin/python3

#
# Complete the maximumProfit function below.
#
def maximumProfit(p):
    return maxP(p, [])


def maxP(p, l):
    if len(l) == 3:
        res = 1
        for x in l:
            res *= x
        return res
    elif len(l) > 3:
        return -1
    elif not l or max(p) < l[0]:
        return max(maxP(p[:-1], l), maxP(p[:-1], l + [p[-1]]))
    else:
        return -1


if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = maximumProfit(p)
    print(result)
