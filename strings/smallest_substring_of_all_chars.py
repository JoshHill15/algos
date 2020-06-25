# n array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

# Come up with an asymptotically optimal solution and analyze the time and space complexities.

# Example:

# input:  arr = ['x','y','z'], str = "xyyzyzyx"

# output: "zyx"
# Constraints:

# [time limit] 5000ms

# [input] array.character arr

# 1 ≤ arr.length ≤ 30
# [input] string str

# 1 ≤ str.length ≤ 500
# [output] string


def sw(chars, a, left, right):
    curr = ""
    # sliding window
    while right <= len(a):
        window = a[left:right]
        # if window contains all characters thats in chars
        if chars.issubset(set(window)):
            curr = window

        left += 1
        right += 1

    return curr


def get_shortest_unique_substring(arr, str):
   # your code goes here
    chars = set(arr)
    a = list(str)
    shortest = ""

    for i in range(len(a)):
        shortest = sw(chars, a, 0, i+1)
        # if it finds a unique substring
        if shortest:
            return "".join(shortest)
    # if no substring exists
    return shortest


arr = ['x', 'y', 'z']
strs = "xyyzyzyx"

a = ["A", "B", "C"]
b = "ADOBECODEBANCDDD"

c = ["A", "B", "C", "E", "K", "I"]
d = "KADOBECODEBANCDDDEI"

f = ["A"]
g = "A"

print(get_shortest_unique_substring(c, d))
