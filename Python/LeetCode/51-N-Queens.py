import pprint
from copy import copy


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        temp_solution = []
        all_ones = 2 ** n - 1

        def nQueens(column, left_diagonal, right_diagonal, placed):
            if placed == n:
                solutions.append(copy(temp_solution))
                return

            valid_spots = all_ones & ~(column | left_diagonal | right_diagonal)
            while valid_spots != 0:
                current_spot = -valid_spots & valid_spots
                pos = (current_spot & -current_spot).bit_length() - 1
                temp_solution.append("".join(["Q" if i == pos else "." for i in range(n)]))
                valid_spots ^= current_spot
                nQueens((column | current_spot), (left_diagonal | current_spot) >> 1,
                        (right_diagonal | current_spot) << 1, placed + 1)
                temp_solution.pop()

        nQueens(0, 0, 0, 0)

        return solutions


"""
use bitwise operations to speed up backtracking
"""

if __name__ == "__main__":
    n = int(input())
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(Solution().solveNQueens(n))
