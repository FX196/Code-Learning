#!/bin/python3

#
# Complete the canModify function below.
#
def canModify(a):
    for i in range(len(a) - 1):
        n = a[:i] + a[i + 1:]
        if n == sorted(n):
            return "YES"
    return "NO"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canModify(a)

        print(result)
