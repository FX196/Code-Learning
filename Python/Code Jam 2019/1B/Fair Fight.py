import sys
from collections import defaultdict


def solve(k, c, d, n):
    diffs = [abs(c_val - d_val) for c_val, d_val in zip(c, d)]
    fair = [ind for ind, diff in enumerate(diffs) if diff <= k]
    l = len(fair)
    count = 0

    for i in range(n):
        for j in range(i, n):
            for num in fair:
                if num < i and i in fair:
                    fair.remove(i)
                    continue
                else:
                    if num <= j:
                        count += 1
    return count

    # greedily assign pairs


T = int(input())
for i in range(1, T + 1):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    res = solve(k, c, d, n)

    print("Case #{0}: {1}".format(i, res))
    sys.stdout.flush()
