import sys


def solve(s):
    return "".join(["E" if c == "S" else "S" for c in s])


T = int(input())
for i in range(T):
    n = input()
    s = input()
    m = solve(s)
    print("Case #{0}: {1}".format(i + 1, m))
    sys.stdout.flush()
