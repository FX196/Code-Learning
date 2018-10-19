import collections
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = collections.defaultdict(set)
        for i, num in enumerate(nums):
            self.data[num].add(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.sample(self.data[target], 1)[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
