s = "h e l l o".split()
s2 = "s p r i n t".split()


def rev(arr):
    a = 0
    b = len(arr)-1

    while a < b:
        arr[a], arr[b] = arr[b], arr[a]
        a += 1
        b -= 1

    return "".join(arr)


print(rev(s2))
