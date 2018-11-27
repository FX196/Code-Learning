from collections import defaultdict
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = defaultdict(int)
        for ind, x in enumerate(S):
            d[x] = ind
        return "".join(sorted(list(T), key=lambda x: d[x]))

    """
    speed of using defualtdict and find depends on the length of S
    """
