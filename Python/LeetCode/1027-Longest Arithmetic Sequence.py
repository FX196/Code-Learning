class Solution:
    def longestArithSeqLength(self, a) -> int:
        maxi = 0
        for i in range(len(a) - 2):
            maxi = max(maxi, self.longestH(a[i:]))
        return maxi

    def longestH(self, l):
        return max(self.longestHp(l, i) for i in range(1, len(l)))

    def longestHp(self, l, ind):
        curr_len = 2
        diff = l[ind] - l[0]
        curr = l[ind]
        l = l[ind + 1:]
        while l:
            if curr + diff in l:
                f = l.index(curr + diff)
                curr_len += 1
                curr += diff
                l = l[f + 1:]
            else:
                return curr_len
        return curr_len


l = [24, 13, 1, 100, 0, 94, 3, 0, 3]
s = Solution()
print(s.longestArithSeqLength(l))
