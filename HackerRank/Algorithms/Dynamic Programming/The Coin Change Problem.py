#!/bin/python3


def getWaysDict(n, c, dict):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in dict:
        return dict[n]
    elif n == min(c):
        dict[min(c)] = 1
        return 1
    else:
        res = 0
        for coin in c:
            res += getWaysDict(n - coin, c, dict)
            if n not in c:
                res -= getWaysDict(coin, c, dict) - 1
        dict[n] = res
        return res


def getWaysMem(sum, coins, coin_num):
    pass


def getWays(n, c):
    res = getWaysDict(n, c, {})
    print(res)


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
