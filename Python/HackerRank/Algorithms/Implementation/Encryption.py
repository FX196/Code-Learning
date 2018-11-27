#!/bin/python3
import math


def encryption(s):
    n = len(s)
    cols = int(math.ceil(n ** 0.5))
    rows = int(math.floor(n ** 0.5))
    if rows * cols < n:
        rows += 1
    res = ""
    for i in range(cols):
        for j in range(rows):
            if j * cols + i < n:
                res += s[j * cols + i]
        res += " "
    return res[:-1]


if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
