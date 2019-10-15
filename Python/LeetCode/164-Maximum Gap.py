from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxG = 0
        for i in range(len(nums) - 1):
            maxG = max(maxG, nums[i + 1] - nums[i])
        return maxG
