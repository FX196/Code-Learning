from functools import lru_cache
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)

        @lru_cache(None)
        def iscat(word):
            for i in range(1, len(word)):
                pre, suf = word[:i], word[i:]
                if ((pre in s) or iscat(pre)) and ((suf in s) or iscat(suf)):
                    return True
            return False

        return [word for word in words if iscat(word)]
