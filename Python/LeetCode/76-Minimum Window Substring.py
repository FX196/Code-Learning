from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        missing = len(t)
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        i = left = right = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not right or j - i <= right - left:
                    left, right = i, j
        return s[left:right]


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
