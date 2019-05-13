class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or 2 * m <= n: return 0
        for i in range(m + 1, n + 1):
            m &= i
        return m
