class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = list(range(1, len(nums) + 2))
        for num in cand:
            if num not in nums:
                return num


"""
It's easy to realize that the first missing positive must be smaller than len(nums)
We can simply iterate over a list of positive integers in range(1,len(nums)+2) and return the first one that's not in nums
"""
