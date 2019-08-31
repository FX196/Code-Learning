from functools import lru_cache
from timeit import timeit


@lru_cache(None)
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    res = 0
    if not m or not n:
        return 1
    if m:
        res += uniquePaths(m - 1, n)
    if n:
        res += uniquePaths(m, n - 1)
    return res


def uniquePaths2(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[1 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

if __name__ == "__main__":
    print(timeit("uniquePaths(20, 20)", number=1000000, setup="from __main__ import uniquePaths"))
