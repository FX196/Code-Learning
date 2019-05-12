class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 1  # nums[i:j] can be visited in cnt jumps
        n = len(nums)
        for cnt in range(1, n):
            i, j = j, max([k + nums[k] + 1 for k in range(i, j)] + [k])
            if j >= n:
                return cnt
        return 0
