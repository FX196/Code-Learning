class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        lens = bin(N)[2:].split('1')[1:-1]
        return max(list(map(len, lens)) + [-1]) + 1
