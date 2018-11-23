class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        all_ones = 2 ** n - 1

        def nQueens(column, left_diagonal, right_diagonal, placed):
            if placed == n:
                self.count += 1
                return

            valid_spots = all_ones & ~(column | left_diagonal | right_diagonal)
            while valid_spots != 0:
                current_spot = -valid_spots & valid_spots
                pos = (current_spot & -current_spot).bit_length() - 1
                valid_spots ^= current_spot
                nQueens((column | current_spot), (left_diagonal | current_spot) >> 1,
                        (right_diagonal | current_spot) << 1, placed + 1)

        nQueens(0, 0, 0, 0)

        return self.count
