import functools
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num] + [1]

        @functools.lru_cache(None)
        def dp(i, j):  # maximum for popping nums[i:j]
            if j - i == 1: return 0
            return max(nums[i] * nums[k] * nums[j] +
                       dp(i, k) + dp(k, j) for k in range(i + 1, j))

        return dp(0, len(nums) - 1)
