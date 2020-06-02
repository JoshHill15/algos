# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows):
    start = [[1], [1, 1]]
    if numRows == 0:
        return []

    elif numRows == 1:
        return [[1]]

    elif numRows == 2:
        return start

    a = 0
    b = 1

    for num in range(numRows-2):
        new_arr = start[-1]
        final_arr = [0] * (len(new_arr) + 1)
        final_arr[0] = 1
        final_arr[-1] = 1
        c = 1
        while b <= len(new_arr):
            first_elem, second_elem = new_arr[a:b+1]
            total = first_elem+second_elem
            final_arr[c] = total
            a += 1
            b += 1
            c += 1

            if b == len(new_arr):
                a = 0
                b = 1
                start.append(final_arr)
                break

    return start


print(generate(5))
