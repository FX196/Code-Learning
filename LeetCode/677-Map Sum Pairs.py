from collections import Counter


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.score = Counter()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        delta = val - self.d.get(key, 0)
        self.d[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.score[prefix]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
