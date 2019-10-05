class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.lines1 = [0]*(2*n+2)
        self.lines2 = [0]*(2*n+2)
        # r1, r2, r3, c1, c2, c3, dmaj, dmin

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            lines = self.lines1
        else:
            lines = self.lines2
        lines[row] +=1
        lines[col + self.n] +=1
        if row == col:
            lines[self.n*2] +=1
        if row == self.n-1-col:
            lines[self.n*2+1] +=1
        if self.n in lines:
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)