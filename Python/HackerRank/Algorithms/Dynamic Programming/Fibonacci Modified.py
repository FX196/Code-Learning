#!/bin/python3

def fibonacciModified(t1, t2, n):
    for i in range(n - 2):
        t1, t2 = t2, t1 + t2 ** 2
    return t2


if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)
