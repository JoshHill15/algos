def cc(s):
    i = 1
    cnt = 1
    left = 0

    while i < len(s):
        if s[i] == s[i-1]:
            cnt += 1

        elif cnt >= 3:
            s = s[:left] + s[i:]
            i = 0
            cnt = 1
            left = 0

        else:
            left = i
            cnt = 1

        i += 1

    return s if cnt < 3 else ""

    # l
    # i
# aabbbacd


a = "aabbbacd"  # cd
b = "aaabbbc"  # c
c = "aabbccddeeeeeedcba"  # ""
d = "aaabbbacd"  # acd
print(cc(c))
