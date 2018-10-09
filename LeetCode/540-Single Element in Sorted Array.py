class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) >= 2 and nums[0] == nums[1]:
            nums = nums[2:]
        return nums[0]
