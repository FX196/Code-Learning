class Solution:
    def isMatch(self, s, p):
        mem = {}  # caches results for isMatch(s[i:], p[j:])

        def dp(i, j):
            if (i, j) not in mem:
                if j == len(p):  # reached the end of p
                    res = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], "."}  # the first characters of s and p match
                    if j + 1 < len(p) and p[j + 1] == "*":
                        # second character in p is *, so either it's
                        # 0 times the first character or many times the first character
                        res = dp(i, j + 2) or first_match and dp(i + 1, j)
                        # can work either way, so it's or between the two conditions
                    else:
                        res = first_match and dp(i + 1, j + 1)
                mem[i, j] = res
            return mem[i, j]

        return dp(0, 0)


if __name__ == "__main__":
    s = input()
    p = input()
    result = Solution().isMatch(s, p)
    print(result)
