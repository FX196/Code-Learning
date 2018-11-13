class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: (-len(x), x))
        s_length = len(s)
        for word in d:
            w = word
            s_ind = -1
            while w:
                s_ind = s.find(w[0], s_ind + 1, s_length)
                if s_ind == -1:
                    break
                w = w[1:]
            if not w:
                return word
        return ""
