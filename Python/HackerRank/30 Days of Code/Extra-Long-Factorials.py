def ExtraLongFactorials(n):
    if n > 1:
        return n * ExtraLongFactorials(n - 1)
    else:
        return 1


if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
