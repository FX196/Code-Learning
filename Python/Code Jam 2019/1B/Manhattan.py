import sys


def solve(consx, consy, q):
    # find x
    nums_x = [sum([cons(x) for cons in consx]) for x in range(q)]
    max_x = 0
    max_ind_x = 0
    for i in range(q):
        if nums_x[i] > max_x:
            max_x = nums_x[i]
            max_ind_x = i

    nums_y = [sum([cons(y) for cons in consy]) for y in range(q)]
    max_y = 0
    max_ind_y = 0
    for i in range(q):
        if nums_y[i] > max_y:
            max_y = nums_y[i]
            max_ind_y = i

    return str(max_ind_x) + " " + str(max_ind_y)


options = {
    "N": lambda y: lambda z: 1 if z > y else 0,
    "S": lambda y: lambda z: 1 if z < y else 0,
    "E": lambda x: lambda z: 1 if z > x else 0,
    "W": lambda x: lambda z: 1 if z < x else 0,
}

T = int(input())
for i in range(1, T + 1):
    n, q = map(int, input().split())
    constraints_x = []
    constraints_y = []
    for _ in range(n):
        x, y, dir = input().split()
        x, y = int(x), int(y)
        if dir in "NS":
            constraints_y.append(options[dir](y))
        else:
            constraints_x.append(options[dir](x))

    res = solve(constraints_x, constraints_y, q)

    print("Case #{0}: {1}".format(i, res))
