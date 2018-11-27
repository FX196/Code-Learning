class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        min_flips = S.count("1")
        ones = 0
        for i, c in enumerate(S):
            if ones > min_flips:
                return min_flips
            elif c == "1":
                min_flips = min(min_flips, S[i:].count("0") + ones)
                ones += 1
        return min_flips


if __name__ == "__main__":
    inp = input()
    print(Solution().minFlipsMonoIncr(inp))
