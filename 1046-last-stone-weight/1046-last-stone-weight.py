class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if stone1 == stone2:
                continue
            stone1 -= stone2
            heapq.heappush(stones, -1 * stone1)
        return -1 * stones[0] if len(stones) == 1 else 0