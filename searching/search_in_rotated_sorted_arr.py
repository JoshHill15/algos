from typing import List

#4 <= 0 < 7 or 0 < 7 < 4 or 7 < 4 < 0
#                 m
# [4, 5, 6, 7, 0, 1, 2]


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] == target:
                return mid
            # go left:
            if nums[0] <= target < nums[mid] or nums[mid] < nums[0] <= target or target < nums[mid] < nums[0]:
                hi = mid - 1

            # go right
            else:
                lo = mid + 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(Solution().search(nums, target))
