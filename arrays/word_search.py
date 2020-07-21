def find_word(board, row, col, word):
    if not word:
        return True

    if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
        return False

    if board[row][col] != word[0]:
        return False

    tmp = board[row][col]
    board[row][col] = "*"

    result = (find_word(board, row-1, col, word[1:]) or
              find_word(board, row, col+1, word[1:]) or
              find_word(board, row+1, col, word[1:]) or
              find_word(board, row, col-1, word[1:]))

    board[row][col] = tmp
    return result


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    found = find_word(board, row, col, list(word))
                    if found:
                        return True

        return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
board2 = [["a"]]
board3 = [["a", "b"], ["c", "d"]]
board33 = [["a", "b"], ["c", "d"]]
board4 = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]


word = "ABCB"
word2 = "ABCCED"
word3 = "SEE"
word4 = "a"
word5 = "abcd"
word6 = "AAB"

print("mine", Solution().exist(board4, word6))


def exist(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position


def dfs(board, i, j, word):
    if len(word) == 0:  # all the characters are checked
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian
    # check whether can find "word" along one direction
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) \
        or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res


print("fin", exist(board33, word5))
