unsorted_scores = [37, 89, 65, 65, 65, 65, 65, 65, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100


def func(scores, highest):
    arr = [0] * highest

    for i in range(len(scores)):
        arr[scores[i]] += 1

    a = 0
    for i in range(len(arr)-1, -1, -1):
        while arr[i] > 0:
            scores[a] = i
            a += 1
            arr[i] -= 1

    return scores


print(func(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
