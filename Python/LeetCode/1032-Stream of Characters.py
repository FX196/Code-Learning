from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.d = defaultdict(TrieNode)
        self.isKey = False

    def insert(self, word):
        if len(word) == 0:
            pass
        if len(word) == 1:
            self.d[word].insert(word)
            self.d[word].isKey = True
        else:
            k, word = word[0], word[1:]
            self.d[k].insert(word)


class StreamChecker:

    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.root.insert(word)
        self.curr = self.root

    def query(self, letter: str) -> bool:
        if letter in self.curr.d.keys():
            self.curr = self.curr.d[letter]
            return self.curr.isKey
        else:
            self.curr = self.root
            return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

# TODO
