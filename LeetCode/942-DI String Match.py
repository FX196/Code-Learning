class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        bank = list(range(len(S) + 1))
        res = []
        for char in S:
            if char == "D":
                res.append(bank.pop())
            else:
                res.append(bank.pop(0))
        return res + bank


"""
greedily add numbers from the list of possible numbers
"""
