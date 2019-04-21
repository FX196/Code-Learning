import sys
from collections import defaultdict


def solve(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    counts = [v for k, v in d.items()]
    counts = list(map(lambda x: x % 2, counts))
    return 1 if sum(counts) <= 1 else 0


T = int(input())
for i in range(T):
    n, q = map(int, input().split())
    c = 0
    s = input()
    for _ in range(q):
        a, b = map(int, input().split())
        c += solve(s[a-1:b])
    print("Case #{0}: {1}".format(i + 1, c))
    sys.stdout.flush()
