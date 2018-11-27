class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        pre_subsets = self.subsets(nums[:-1])
        res = pre_subsets + [subset + [nums[-1]] for subset in pre_subsets]
        return res
