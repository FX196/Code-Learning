import math


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(math.pow(2, int(math.log(num, 2) + 1)) - 1 - num)
        """
        first part is basically a bunch of 1's
        e.g. for example, if num=5
        then 111-101=010
        """
