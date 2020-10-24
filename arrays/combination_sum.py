from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int, curr=None, ans=None) -> List[List[int]]:
        if not ans and not curr:
            curr = []
            ans = []

        if target == 0:
            ans.append(curr)

        for i, c in enumerate(candidates):
            if c <= target:
                self.combinationSum(
                    candidates[i:], target - c, curr + [c], ans)

        return ans


s = Solution()
arr = [2, 3, 6, 7]
t = 7
print(s.combinationSum(arr, t))
