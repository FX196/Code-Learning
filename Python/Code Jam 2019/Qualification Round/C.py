import sys
from math import gcd


def solve(nums):
    ans = []
    n = int(nums[0] / gcd(nums[0], nums[1]))
    for num in nums:
        ans.append(n)
        n = int(num / n)
    ans.append(n)
    primes = list(set(ans))
    keys = {v: chr(65 + i) for i, v in enumerate(sorted(primes))}
    res = [keys[x] for x in ans]
    return "".join(res)


def solve2(nums):
    ans = [gcd(nums[i], nums[i + 1]) for i in range(len(nums) - 1)]
    ans = [nums[0] // ans[0]] + ans + [nums[-1] // ans[-1]]
    primes = list(set(ans))
    keys = {v: chr(65 + i) for i, v in enumerate(sorted(primes))}
    res = [keys[x] for x in ans]
    return "".join(res)


def solve3(nums, n):
    ans = []
    primes = set()
    r = nums[0] // (gcd(nums[0], nums[1]) % n)
    r = n if r == 0 else r
    ans.append(r)
    for i in range(len(nums)):
        primes.add(ans[i])
        r = (nums[i] // ans[i]) % n
        r = n if r == 0 else r
        ans.append(r)
    primes.add(ans[-1])
    keys = {v: chr(65 + i) for i, v in enumerate(sorted(primes))}
    res = [keys[x] for x in ans]
    return "".join(res)


T = int(input())
for i in range(1, T + 1):
    n, l = map(int, input().split())
    nums = list(map(int, input().split()))
    res = solve3(nums, n)

    print("Case #{0}: {1}".format(i, res))
    sys.stdout.flush()
