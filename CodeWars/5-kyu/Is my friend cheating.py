def removNb(n):
    # your code
    su = n*(n+1)/2
    res = []
    for j in range(1, n+1):
        s = su-j
        i=j+1
        if s/i == int(s/i) and s/i <= n:
            res.append((j,int(s/i)))
    return res