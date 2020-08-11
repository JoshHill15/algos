a = [(1, 2), (2, 3)]
b = [(1, 5), (2, 3)]
c = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
d = [(1, 10), (2, 6), (3, 5), (7, 9)]
e = [(1, 3), (2, 4)]


def condense(arr):
    final = []
    orig_end = arr[0][1]
    orig_start = arr[0][0]
    arr.sort(key=lambda x: x[0])

    for i in range(1, len(arr)):
        start_time, end_time = arr[i]

        if orig_end < start_time:
            if not final:
                final.append((orig_start, orig_end))

            elif final and (orig_start, orig_end) != final[-1]:
                final.append((orig_start, orig_end))

            orig_start = start_time
            orig_end = end_time

        elif orig_end >= start_time and orig_end < end_time:
            final.append((orig_start, end_time))
            orig_end = end_time

    return final or [arr[0]]


print(condense(a))
print(condense(b))
print(condense(c))
print(condense(d))
print(condense(e))
