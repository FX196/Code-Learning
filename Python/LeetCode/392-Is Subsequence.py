class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        while s:
            ind = t.find(s[0])
            if ind == -1:
                return False
            else:
                t = t[ind + 1:]
            s = s[1:]
        return not s
