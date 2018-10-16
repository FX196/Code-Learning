from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if not s or not words:
            return res
        word_length = len(words[0])
        word_num = len(words)

        total_length = word_length * word_num

        for i in range(0, len(s) - total_length + 1):
            word_window = s[i:i + total_length]
            window_words = [word_window[j:j + word_length] for j in range(0, total_length, word_length)]
            if Counter(window_words) == Counter(words):
                res.append(i)
        return res

# Time Limit Exceeded TODO
