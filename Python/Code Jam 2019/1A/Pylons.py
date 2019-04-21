import sys


def solve(rows, cols, r, c):
    deltas = [
        (2, 1),
        (1, 2),
        (1, -2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (-1, -2),
        (-2, -1),
    ]



T = int(input())
for i in range(T):
    n = input()
    m = solve(n)
    print("Case #{0}: {1}".format(i + 1, m))
    sys.stdout.flush()
