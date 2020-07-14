def cnt_islands(grid, row, col, cnt):
    if row == len(grid) or col == len(grid[0]) or row < 0 or col < 0:
        print("1", cnt)
        return cnt

    if grid[row][col] == 0 or grid[row][col] == "*":
        print("2", cnt)
        return cnt

    grid[row][col] = "*"

    if row-1 == -1 or grid[row-1][col] == 0:
        cnt += 1

    if row+1 == len(grid) or grid[row+1][col] == 0:
        cnt += 1

    if col-1 == -1 or grid[row][col-1] == 0:
        cnt += 1

    if col+1 == len(grid[0]) or grid[row][col+1] == 0:
        cnt += 1

    up = cnt_islands(grid, row-1, col, cnt)
    down = cnt_islands(grid, row+1, col, cnt)
    left = cnt_islands(grid, row, col-1, cnt)
    right = cnt_islands(grid, row, col+1, cnt)

    total = max(up, down, left, right)
    return up and down and left and right


class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return cnt_islands(grid, row, col, cnt)


a = [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]

print(Solution().islandPerimeter(a))
