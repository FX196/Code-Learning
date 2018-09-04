#!/bin/python3

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 2, -1, -1):
        j = i
        while j < (len(q) - 1):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                bribes += 1
                j += 1
                if (j - i) > 2:
                    print("Too chaotic")
                    return
            else:
                break
    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
