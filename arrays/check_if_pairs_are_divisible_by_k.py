from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for a in arr:
            a %= k
            theOther = (k - a) % k
            if cnt[theOther] > 0:
                cnt[theOther] -= 1
            else:
                cnt[a] += 1
        return all(c == 0 for c in cnt)


a = [1, 2, 3, 4, 5, 6]
print(Solution().canArrange(a, 10))
