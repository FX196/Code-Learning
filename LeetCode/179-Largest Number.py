class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int("".join(
            sorted(map(str, nums), cmp=lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0, reverse=True))))
