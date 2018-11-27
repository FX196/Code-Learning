class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        res = []
        for i in range(len(s) - 9):
            substr = s[i:i + 10]
            if substr not in d.keys():
                d[substr] = 1
            elif d[substr] == 1:
                d[substr] += 1
                res.append(substr)
        return res
