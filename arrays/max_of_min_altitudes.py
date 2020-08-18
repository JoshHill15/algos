from typing import List
a = [[1, 2, 3],
     [4, 5, 1]]


def min_val(arr):
    path = []
    bottom = len(a)-1
    right = len(a[0])-1

    x, y = 0, 0

    while x != bottom or y != right:
        value = arr[x][y]
        path.append(value)

        if x+1 <= bottom:
            value_below = arr[x+1][y]

        if y+1 <= right:
            value_right = arr[x][y+1]

        larger = max(value_below, value_right)
        if larger == arr[x+1][y]:
            x += 1
        else:
            y += 1

    path.append(arr[x][y])

    print(path)
    return min(path)


class Solution:
    def fill_zeroes(self, matrix, row, col):
        # right
        for i in range(len(matrix[0])):
            print("first", matrix, (row, i))
            matrix[row][i] = 0

        # # left
        # for i in range(0, col):
        #     print("sec", matrix, (row, i))
        #     matrix[row][i] = 0

        # # up
        # for i in range(0, row):
        #     print("t", matrix, (i, col))
        #     matrix[i][col] = 0

        # down
        for i in range(len(matrix)):
            print("f", matrix, (i, col))
            matrix[i][col] = 0

        print(matrix)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        height, width = len(matrix), len(matrix[0])

        for row in range(height):
            for col in range(width):
                if matrix[row][col] == 0:
                    zeros.append((row, col))

        for row, col in zeros:
            self.fill_zeroes(matrix, row, col)

    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = -1000000
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    # We modify the elements in place. Note, we only change the non zeros to MODIFIED
                    for k in range(C):
                        matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
                    for k in range(R):
                        matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0
        for r in range(R):
            for c in range(C):
                # Make a second pass and change all MODIFIED elements to 0 """
                if matrix[r][c] == MODIFIED:
                    matrix[r][c] = 0


# print(min_val(a))
aa = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
b = [[1, 3, 0]]
# print(Solution().setZeroes(aa))

c = ['Waltz', 'walt', 'Tango', 'Viennese Waltz', 'Foxtrot',
     'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']


c.sort(key=lambda elem: elem[len(elem) // 2], reverse=True)

for word in c:
    print(word)

# 'Cha Cha'
# 'Paso Doble'
# 'Viennese Waltz'
# 'Waltz'
# 'Samba'
# 'Rumba'
# 'Tango'
# 'Foxtrot'
# 'Jive'
