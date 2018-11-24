class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        present_arr = [False] * (len(nums) + 1)
        present_arr[0] = True
        for num in nums:
            present_arr[num] = True
        return [element for element, present in enumerate(present_arr) if not present]
