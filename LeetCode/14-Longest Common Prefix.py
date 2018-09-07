class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        if not strs:
            return ""
        l = len(min(strs, key=len))
        while i < l:
            if len(set([s[i] for s in strs])) == 1:
                i += 1
            else:
                break
        return strs[0][:i] if i != l else min(strs, key=len)
