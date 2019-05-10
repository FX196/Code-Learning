import math
from random import random


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        rand_r = random() * math.pi * 2
        rand_l = (random() ** 0.5) * self.r
        return [self.x + rand_l * math.cos(rand_r), self.y + rand_l * math.sin(rand_r)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
