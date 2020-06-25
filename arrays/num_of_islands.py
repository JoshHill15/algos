def dfs(grid, i, j, v):
    if i < 0 or j < 0 or j > len(grid[0]) or i > len(grid):
        return

    v.add((i, j))
    if grid[i][j] == "1":
        grid[i][j] = "*"

    if i > 0 and grid[i-1][j] == "1":
        dfs(grid, i-1, j, v)

    if i < len(grid)-1 and grid[i+1][j] == "1":
        dfs(grid, i+1, j, v)

    if j > 0 and grid[i][j-1] == "1":
        dfs(grid, i, j-1, v)

    if j < len(grid[0])-1 and grid[i][j+1] == "1":
        dfs(grid, i, j+1, v)

    return


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        v = set()
        r = len(grid[0])
        c = len(grid)
        count = 0

        for i in range(c):
            for j in range(r):
                if grid[i][j] == "1" and (i, j) not in v:
                    dfs(grid, i, j, v)
                    count += 1

        return count


s = Solution()

a = [[1, 1, 1, 1, 0],
     [1, 1, 0, 1, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0]]


c = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

b = s.numIslands(c)
print(b)
