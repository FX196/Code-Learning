#!/bin/python3


def equal(arr):
    count = 0
    m = min(arr)
    for i in range(len(arr)):
        arr[i] -= m
        while arr[i] != 0:
            for v in (5, 3, 1):
                if arr[i] >= v:
                    count += arr[i] // v
                    arr[i] = arr[i] % v
    return count


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = equal(arr)
        print(result)
