import string


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = str.maketrans(dict.fromkeys(string.punctuation))
        s = s.translate(table)
        s = s.replace(" ", "").lower()
        return s == s[::-1]
