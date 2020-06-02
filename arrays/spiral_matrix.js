// Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

// Example 1:

// Input:
// [
//  [ 1, 2, 3 ],
//  [ 4, 5, 6 ],
//  [ 7, 8, 9 ]
// ]
// Output: [1,2,3,6,9,8,7,4,5]
// Example 2:

// Input:
// [
//   [1, 2, 3, 4],
//   [5, 6, 7, 8],
//   [9,10,11,12]
// ]
// Output: [1,2,3,4,8,12,11,10,9,5,6,7]

var spiralOrder = function (matrix) {
  if (matrix.length < 1 || matrix == null) {
    return []
  }

  const size = matrix[0].length * matrix.length
  const ans = []

  let left = 0
  let top = 0
  let right = matrix[0].length - 1
  let bottom = matrix.length - 1

  // while (ans.length < size) {
  while (left <= right && top <= bottom) {

    for (let i = left; i <= right; i++) {
      if (ans.length == size) return ans
      else ans.push(matrix[top][i])
    }
    top++

    for (let i = top; i <= bottom; i++) {
      if (ans.length == size) return ans
      else ans.push(matrix[i][right])
    }
    right--

    for (let i = right; i >= left; i--) {
      if (ans.length == size) return ans
      else ans.push(matrix[bottom][i])
    }
    bottom--

    for (let i = bottom; i >= top; i--) {
      if (ans.length == size) return ans
      else ans.push(matrix[i][left])
    }
    left++
  }
  return ans
};

console.log(spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]))