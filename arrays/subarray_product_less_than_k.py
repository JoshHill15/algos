from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        product = 1
        sub_arrays = 0

        while left < len(nums):
            product *= nums[right] if right < len(nums) else k

            if product < k:
                sub_arrays += 1
                right += 1

            else:
                left += 1
                right = left
                product = 1

        return sub_arrays

    def numSubarrayProductLessThanK2(self, nums, k):

        if k <= 1:
            return 0

        count = 0
        left = 0
        prod = 1

        for right, n in enumerate(nums):
            prod *= n
            while prod >= k:
                prod //= nums[left]
                left += 1

            count += right - left + 1

        return count


nums = [10, 5, 2, 6]
k = 100
print(Solution().numSubarrayProductLessThanK2(nums, k))
