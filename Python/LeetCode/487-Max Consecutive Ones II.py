from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # keep track of the last two zeros and a current max
        prev_zero, pprev_zero = -1, -1
        max_len = 0
        for ind, num in enumerate(nums):
            if num == 0:
                max_len = max(max_len, ind - pprev_zero - 1)
                pprev_zero, prev_zero = prev_zero, ind
        return max(max_len, ind - pprev_zero)
