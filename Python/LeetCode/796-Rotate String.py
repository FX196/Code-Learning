class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return (A + A).find(B) != -1 and len(A) == len(B)
