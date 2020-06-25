# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board
#  are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O'
# on the border will be flipped to 'X'. Two cells are connected if they are adjacent
# cells connected horizontally or vertically.


def dfs(board, i, j, row, col):
    if i < 0 or j < 0 or j == row or i == col:
        return

    if board[i][j] == "O":
        board[i][j] = "safe"

    if i < col-1 and board[i+1][j] == "O":
        dfs(board, i+1, j, row, col)

    if i > 0 and board[i-1][j] == "O":
        dfs(board, i-1, j, row, col)

    if j < row-1 and board[i][j+1] == "O":
        dfs(board, i, j+1, row, col)

    if j > 0 and board[i][j-1] == "O":
        dfs(board, i, j-1, row, col)

    return


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        col = len(board)
        row = len(board[0])

        for i in range(col):
            if board[i][row-1] == "O":
                dfs(board, i, row-1, row, col)

            if board[i][0] == "O":
                dfs(board, i, 0, row, col)

        for i in range(row):
            if board[0][i] == "O":
                dfs(board, 0, i, row, col)

            if board[col-1][i] == "O":
                dfs(board, col-1, i, row, col)

        for i in range(col):
            for j in range(row):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "safe":
                    board[i][j] = "O"


s = Solution()
a = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
     ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

b = [["O", "O"], ["O", "O"]]
c = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], [
    "X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]

d = [["O", "O", "O", "O", "X", "X"], ["O", "O", "O", "O", "O", "O"], ["O", "X", "O", "X", "O", "O"], [
    "O", "X", "O", "O", "X", "O"], ["O", "X", "O", "X", "O", "O"], ["O", "X", "O", "O", "O", "O"]]

e = [["O", "O", "O", "O", "X", "X"], ["O", "O", "O", "O", "O", "O"], ["O", "X", "O", "X", "O", "O"], [
    "O", "X", "O", "O", "X", "O"], ["O", "X", "O", "X", "O", "O"], ["O", "X", "O", "O", "O", "O"]]

s.solve(c)
