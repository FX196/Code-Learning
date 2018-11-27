t = int(input().strip())
for a0 in range(t):
    max = 0
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if i & j > max and i & j < k:
                max = i & j
    print(str(max))
