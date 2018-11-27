class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 1
        while i < (len(nums)):
            if nums[i - 1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return i
