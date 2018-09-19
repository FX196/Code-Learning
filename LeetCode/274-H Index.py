class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return max(
            [0] + [count + 1 for count, index in enumerate(sorted(citations, reverse=True)) if index >= count + 1])
