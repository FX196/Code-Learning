import sys


def solve(n):
    a, b = "", ""
    for c in n:
        if c == "4":
            a+="2"
            b+="2"
        else:
            a+=c
            b+="0"
    return " ".join([str(int(a)), str(int(b))])


T = int(input())
for i in range(T):
    n = input()
    m = solve(n)
    print("Case #{0}: {1}".format(i + 1, m))
    sys.stdout.flush()
