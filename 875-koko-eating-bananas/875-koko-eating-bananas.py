import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = (high + low) // 2
            ans = 0
            for p in piles:
                ans += math.ceil(p/mid)
            if ans <=h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return  res