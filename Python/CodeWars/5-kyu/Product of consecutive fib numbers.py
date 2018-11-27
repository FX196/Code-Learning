def productFib(prod):
    # your code
    l, m, n = 0, 0, 1
    while m * n < prod:
        l, m, n = m, n, m + n
    return [m, n, m * n == prod]
