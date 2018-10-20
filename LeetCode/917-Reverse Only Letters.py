import string


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i] not in string.ascii_letters:
                i += 1
            elif s[j] not in string.ascii_letters:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)
