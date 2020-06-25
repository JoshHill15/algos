# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

# -2 (K)	-3	3
# -5	-10	1
# 10	30	-5 (P)


# Note:

# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.


def calculateMinimumHP(dungeon):
    # If at any point his health point drops to 0 or below, he dies immediately.
    # have to make sure at any point health is > 0
    # dp[i][j] is minimum health needed when arriving at this grid
    #dp[i][j] = min(max(1, dp[right]-right_grid_value), max(1, dp[down]-down_grid_value))
    row, col = len(dungeon), len(dungeon[0])
    dp = [[0 for x in range(col)] for x in range(row)]
    dp[row-1][col-1] = 1

    for i in range(row-2, -1, -1):
        dp[i][col-1] = max(1, dp[i+1][col-1]-dungeon[i+1][col-1])

    for i in range(col-2, -1, -1):
        dp[row-1][i] = max(1, dp[row-1][i+1]-dungeon[row-1][i+1])

    for i in range(row-2, -1, -1):
        for j in range(col-2, -1, -1):
            right = max(1, dp[i][j+1]-dungeon[i][j+1])
            down = max(1, dp[i+1][j]-dungeon[i+1][j])
            dp[i][j] = min(right, down)

    return max(1, dp[0][0]-dungeon[0][0])


print(calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
