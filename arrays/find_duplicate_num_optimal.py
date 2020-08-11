
a = [2, 3, 1, 3]  # 3
b = [3, 4, 2, 3, 1, 5]  # 3
c = [3, 1, 2, 2]  # 2
d = [4, 3, 1, 1, 4]  # 4 and 1
n = [6, 4, 5, 6, 2, 3, 1]


def find_duplicate(arr):
    n = len(arr) - 1
    position = n+1

    for i in range(n):
        position = arr[position-1]

    current_position = arr[position-1]
    cnt = 1

    while current_position != position:
        current_position = arr[current_position-1]
        cnt += 1

    starter_pointer = n+1
    farther_pointer = n+1

    for i in range(cnt):
        farther_pointer = arr[farther_pointer-1]

    while starter_pointer != farther_pointer:
        starter_pointer = arr[starter_pointer-1]
        farther_pointer = arr[farther_pointer-1]

    return starter_pointer


e = [a, b, c, d, n]

for arr in e:
    ans = find_duplicate(arr)
    print(ans)
