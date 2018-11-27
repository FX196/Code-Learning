class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = [0] * (len(nums) + 1)
        res = []
        for i in nums:
            if dup[i]:
                res.append(i)
            else:
                dup[i] = 1
        return res
