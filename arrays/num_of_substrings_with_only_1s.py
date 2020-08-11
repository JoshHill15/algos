print("caled")


def sw(s, right, compare):
    cnt = 0
    left = 0
    while right <= len(s):
        window = s[left:right]
        if window == compare:
            cnt += 1

        right += 1
        left += 1

    return cnt


class Solution:
    def numSub(self, s: str) -> int:
        compare = ["1"]
        cnt = 0
        s = list(s)

        for i in range(len(s)):
            cnt += sw(s, i+1, compare)
            compare.append("1")

        return cnt

    def numSub2(self, s):
        return sum(len(a) * (len(a) + 1) / 2 for a in s.split('0')) % (10**9 + 7)

    def numsSub3(self, s):
        v = s.split("0")
        for a in v:
            sum(len(a) * len(a))


print(Solution().numSub2("0110111"))
