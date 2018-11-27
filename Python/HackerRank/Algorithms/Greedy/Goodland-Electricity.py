#!/bin/python3


def pylons(k, arr):
    # Complete this function
    count = 0
    while arr:
        c = arr[0:k]
        found = False
        i = min(k - 1, len(arr) - 1)
        while not found:
            if c[i] == 1:
                count += 1
                found = True
                if len(arr) > i + k - 1:
                    arr = arr[i + k:]
                else:
                    return count
            elif i == 0:
                return -1
            else:
                i -= 1
    return count


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pylons(k, arr)
    print(result)
