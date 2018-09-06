class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            if target - nums[i] in nums[i + 1:]:
                ind = nums.index(target - nums[i], i + 1)
                if i != ind:
                    return [i, ind]
            i += 1
