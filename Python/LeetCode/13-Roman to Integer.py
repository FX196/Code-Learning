class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        i, l1, l2 = 0, len(s), len(s) - 1
        res = 0

        while i < l2:
            if d[s[i]] < d[s[i + 1]]:
                res += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                res += d[s[i]]
                i += 1

        if i < l1:
            res = res + d[s[l2]]

        return res
