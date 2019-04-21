import sys


def solve(r):
    delta_t = r[0][0]
    r = sorted(r, key=lambda x: x[1])


T = int(input())
for i in range(T):
    n = int(input())
    r = []
    for _ in range(n):
        r += list(map(int, input().split()))
    m = solve(r)
    print("Case #{0}: {1}".format(i + 1, m))
    sys.stdout.flush()
