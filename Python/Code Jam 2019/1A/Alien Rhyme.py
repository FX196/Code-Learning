import sys
from collections import defaultdict


class Trie:
    def __init__(self):
        self.dict = defaultdict(Trie)
        self.size = 0

    def insert_word(self, word):
        if word:
            self.dict[word[0]].insert_word(word[1:])
        self.size += 1

    def remove(self):
        if self.size == 0:
            return 0
        count = 0
        for k, v in self.dict.items():
            if v.size >= 2:
                r = v.remove()
                if r > 0:
                    self.size -= v.size
                count += r
        if self.size >= 2:
            return count + 2
        else:
            return count


def solve(words):
    root = Trie()
    for word in words:
        root.insert_word(word[::-1])
    count = 0
    for k, v in root.dict.items():
        count += v.remove()
    return count

    # greedily assign pairs


T = int(input())
for i in range(1, T+1):
    n = int(input())
    words = [input() for _ in range(n)]
    res = solve(words)

    print("Case #{0}: {1}".format(i, res))
    sys.stdout.flush()
