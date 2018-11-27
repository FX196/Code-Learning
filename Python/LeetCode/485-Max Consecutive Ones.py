class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_so_far = 0
        for n in nums:
            if n == 1:
                count += 1
            elif n == 0:
                count, max_so_far = 0, max(count, max_so_far)
        return max(count, max_so_far)
