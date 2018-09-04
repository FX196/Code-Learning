#!/bin/python3

import os


# Complete the hourglassSum function below.
def hourglassSum(arr):
    m, n = len(arr), len(arr[0])
    sums = []
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            sums.append(sum(arr[i - 1][j - 1:j + 2]) + arr[i][j] + sum(arr[i + 1][j - 1:j + 2]))
    return max(sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
