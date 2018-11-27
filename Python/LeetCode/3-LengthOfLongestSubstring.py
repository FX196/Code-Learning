class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        longest = 0
        i, j = 0, 0  # ptr 1 and 2
        while j < len(s):  # keep j in range
            if s[j] in s[i:j]:
                longest = max(longest, j - i)
                while s[j] in s[i:j]:
                    i += 1
            j += 1
        longest = max(longest, j - i)
        return longest


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("dvdf"))
