class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        fibs = [1, 2]
        for _ in range(30):
            fibs.append(fibs[-1] + fibs[-2])
        res = 0
        last = 0
        for k in range(30, -1, -1):
            if num & (1 << k):
                res += fibs[k]
                if last:
                    return res
                last = 1
            else:
                last = 0
        return res + 1

# algorithm from https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/103754/C%2B%2B-Non-DP-O(32)-Fibonacci-solution
