#!/bin/python3


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] == (i + 1):
            i += 1
        else:
            m = min(len(arr), arr[i] - 1)
            arr[m], arr[i] = arr[i], arr[m]
            count += 1
    return count


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)
