class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([int(c) for c in bin(n)[2:]])