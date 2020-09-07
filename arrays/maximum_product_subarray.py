def maxProduct(A):
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1

    concat = A + B
    return max(concat)


a = [0, 2]
b = [2, 3, -2, 4]
c = [-2, 0, -1]
print(maxProduct(c))
