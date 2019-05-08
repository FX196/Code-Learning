import sys
from collections import defaultdict


def solve(words):
    pass

    # greedily assign pairs


T = int(input())
for i in range(1, T+1):
    n = int(input())
    words = [input() for _ in range(n)]
    res = solve(words)

    print("Case #{0}: {1}".format(i, res))
    sys.stdout.flush()
