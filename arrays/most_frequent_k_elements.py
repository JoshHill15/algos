from heapq import heappop, heappush, heapify


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        hm = {}
        result = []

        for num in nums:
            if num in hm:
                hm[num] += 1

            else:
                hm[num] = 1

        for key in hm:
            priority = -hm[key]
            heappush(heap, (priority, key))

        for i in range(k):
            popped = heappop(heap)
            result.append(popped[1])

        return result


a = [2, 3, 4, 1, 4, 0, 4, -1, -2, -1]
k = 2

print(Solution().topKFrequent(a, k))
