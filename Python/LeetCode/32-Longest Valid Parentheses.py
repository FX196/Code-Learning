class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        mem = [0] * l
        for i in range(1, l):
            if s[i] == ")":
                if s[i - 1] == "(":
                    mem[i] = mem[i - 2] + 2
                else:
                    target = i - mem[i - 1] - 1
                    if target >= 0 and s[target] == "(":
                        mem[i] = mem[i - 1] + 2 + mem[target - 1]
        return max(mem) if mem else 0

# dp solution
