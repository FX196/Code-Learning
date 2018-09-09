# TODO: unfinished
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        last = ""
        while s and p:
            if p[-1] == s[-1]:
                s, p = s[:-1], p[:-1]
            elif p[-1] == "*":
                while s[-1] == p[-1]:
                    pass
        else:
            if not s and not p:
                return True
            else:
                return False


if __name__ == "__main__":
    s = input()
    p = input()
    res = Solution.isMatch(Solution, s, p)
    print(res)
