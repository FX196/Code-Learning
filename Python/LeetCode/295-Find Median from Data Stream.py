from heapq import heappush, heappop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.large and num > -self.large[0]:
            heappush(self.small, num)
            if len(self.small) - 1 > len(self.large):
                heappush(self.large, -heappop(self.small))
        else:
            heappush(self.large, -num)
            if len(self.small) < len(self.large) - 1:
                heappush(self.small, -heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        s = len(self.small)
        l = len(self.large)
        if s == l != 0:
            return (self.small[0] - self.large[0]) / 2
        if s == l == 0:
            return 0
        elif s < l:
            return -self.large[0]
        else:
            return self.small[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
