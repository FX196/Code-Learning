from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        out = [1] * length
        prod_left = 1
        prod_right = 1
        for i in range(length):
            out[i] *= prod_left
            prod_left *= nums[i]
        for i in range(length - 1, -1, -1):
            out[i] *= prod_right
            prod_right *= nums[i]
        return out
