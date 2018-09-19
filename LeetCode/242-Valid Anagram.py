class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c in s:
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
        for c in t:
            if c not in d.keys():
                return False
            else:
                d[c] -= 1
        return sum([0 if x[1] == 0 else 1 for x in d.items()]) == 0
