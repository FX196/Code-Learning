from collections import defaultdict


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        chars = sorted(d, key=lambda x: d[x], reverse=True)
        for char in chars:
            res += char * d[char]
        return res
