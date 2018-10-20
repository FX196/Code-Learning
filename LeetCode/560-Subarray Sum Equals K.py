import collections


class Solution(object):
    def subarraySum(self, nums, k):
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
curr_sum = PrefixSum(m)
sum_counts[q] = number of x's such that PrefixSum(x) = q
sum_counts[curr_sum-k] = number of x's such that PrefixSum(m) - k = PrefixSum(x)
PrefixSum(m) - k = PrefixSum(x) is equivalent to PrefixSum(m) - PrefixSum(x) = k,
or IntervalSum(x, m) = k
"""
