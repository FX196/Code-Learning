class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr, max_so_far = 1, 0
        if len(nums) < 2:
            return len(nums)
        if len(nums) == 2:
            return 1 + int(sorted(nums) == nums)
        else:
            for i in range(len(nums) - 1):
                if nums[i] <= nums[i + 1]:
                    curr += 1
                else:
                    max_so_far = max(max_so_far, curr)
                    curr = 1
        return max_so_far
        # TODO
