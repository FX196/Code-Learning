class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = {}
        return self.combinationSumMem(candidates, target, len(candidates) - 1, d)

    def combinationSumMem(self, candidates, target, ind, d):
        if target == 0:
            return [[]]
        elif target < 0:
            return None
        elif ind < 0:
            return None
        elif target in d.keys() and ind in d[target].keys():
            return d[target][ind]
        else:
            if not target in d.keys():
                d[target] = {}
            res = []
            use_ind = self.combinationSumMem(candidates, target - candidates[ind], ind, d)
            not_use_ind = self.combinationSumMem(candidates, target, ind - 1, d)
            if use_ind:
                used_candidate = candidates[ind]
                res += [x + [used_candidate] for x in use_ind]
            if not_use_ind:
                res += not_use_ind
            d[target][ind] = res
            return res


"""
same logic as the coin exchange problem in HackerRank-Algorithms-DynamicProgramming
cache calculated results
for each element in candidates, we can either use this candidate or not use this candidate
calculate the sub-problem for each case and add them together
"""

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
