class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        for num in nums:
            if num != val:
                nums[length] = num
                length += 1
        return length
