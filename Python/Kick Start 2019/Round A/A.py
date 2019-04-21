import sys


def solve(n, p, s):
    min_cost = 10000 * 10 ** 5
    skills = set(s)
    for person in skills:
        sublist = list(filter(lambda x: x <= person, s))
        if len(sublist) < p:
            continue
        sublist.sort(reverse=True)
        min_cost = min(min_cost, person * p - sum(sublist[:p]))
    return min_cost


T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    s = list(map(int, input().split()))
    m = solve(n, p, s)
    print("Case #{0}: {1}".format(i + 1, m))
    sys.stdout.flush()
