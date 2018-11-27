d = {}


def exp_sum(n):
    # your code here
    return count_partition(n, n)


def count_partition(amount, p):
    global d
    if p == 1:
        return 1
    elif amount < 0:
        return 0
    elif amount in d.keys() and p in d[amount].keys():
        return d[amount][p]
    else:
        with_p = count_partition(amount - p, p)
        without_p = count_partition(amount, p - 1)
        if not amount in d.keys():
            d[amount] = {}
        d[amount][p] = with_p + without_p
        return d[amount][p]
