class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        sign = int(x / abs(x))
        res = str(abs(x))[::-1]
        res = int(res) * sign
        return res if (res <= (2 ** 31 - 1) and res >= (-2 ** 31)) else 0
