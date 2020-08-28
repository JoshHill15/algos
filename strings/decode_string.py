class Solution:
    def decodeString(self, s: str) -> str:
        curr_str = ""
        stack = []
        cur_num = 0

        for char in s:
            if char == "[":
                stack.append((curr_str, cur_num))
                cur_num = 0
                curr_str = ""

            elif char == "]":
                prev_str, prev_num = stack.pop()
                curr_str = prev_str + (curr_str * prev_num)

            elif char.isdigit():
                cur_num = cur_num * 10 + int(char)

            else:
                curr_str += char

        return curr_str


a = "3[a]2[bc]"
b = "3[a2[c]]"
c = "abc3[cd]xyz"
d = "100[leetcode]"

print(Solution().decodeString(a))
