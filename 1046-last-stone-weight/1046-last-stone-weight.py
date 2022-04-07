import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 - stone2 == 0:
                continue
            else:
                heapq.heappush(stones, -1 * abs(stone1 - stone2))
        return -1 * stones[0] if stones else 0