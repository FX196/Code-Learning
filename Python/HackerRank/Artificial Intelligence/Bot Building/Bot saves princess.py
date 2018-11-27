#!/usr/bin/python
def displayPathtoPrincess(n, grid):
    b = []
    p = []
    for i in range(len(grid)):
        if 'm' in grid[i]:
            b.append(i)
        if 'p' in grid[i]:
            p.append(i)
    for i in range(len(grid)):
        if grid[b[0]][i] == 'm':
            b.append(i)
        if grid[p[0]][i] == 'p':
            p.append(i)
    while b[0] < p[0]:
        print("DOWN")
        b[0] += 1
    while b[0] > p[0]:
        print("UP")
        b[0] -= 1
    while b[1] > p[1]:
        print("LEFT")
        b[1] -= 1
    while b[1] < p[1]:
        print("RIGHT")
        b[1] += 1


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
