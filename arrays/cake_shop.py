a = [17, 8, 24]
b = [12, 19, 2]
c = [17, 8, 12, 19, 24, 2]

a2, b2, c2 = [1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3]

a3, b3, c3 = [], [4, 3], [3, 4]


def cake(take_out, dine_in, served):
    a, b, c = 0, 0, 0

    while c < len(served):
        if a < len(take_out) and take_out[a] == served[c]:
            a += 1

        elif b < len(dine_in) and dine_in[b] == served[c]:
            b += 1

        else:
            return False

        c += 1

    return True


print(cake(a3, b3, c3))
