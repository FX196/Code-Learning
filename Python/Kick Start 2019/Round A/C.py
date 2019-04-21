import sys


def solve(n, q, s):
    seats = [1]*n
    


T = int(input())
for i in range(T):
    n, q = map(int, input().split())
    s = []
    for _ in range(q):
        a, b = list(map(int, input().split()))
        s.append((a, b))
    ans = solve(n, q, s)
    print("Case #{0}: {1}".format(i + 1, ans))
    sys.stdout.flush()
