class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows > len(s) or numRows == 1:
            return s
        l = [""] * numRows
        index, it = 0, 1
        for x in s:
            if index == 0:
                it = 1
            elif index == numRows - 1:
                it = -1
            l[index] += x
            index += it
        return "".join(l)
