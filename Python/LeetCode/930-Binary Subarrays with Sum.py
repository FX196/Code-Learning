import collections


class Solution(object):
    def numSubarraysWithSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        sum_counts = collections.defaultdict(int)
        sum_counts[0] = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            res += sum_counts[curr_sum - k]
            sum_counts[curr_sum] += 1
        return res


"""
Exactly the same as 560-Subarray Sum Equals K
"""
