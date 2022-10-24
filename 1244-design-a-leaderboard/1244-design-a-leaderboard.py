class Leaderboard:

    def __init__(self):
        
        self.leaderboard= defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        
        self.leaderboard[playerId] += score

    def top(self, K: int) -> int:
        
        res = 0
        heap = []
        for num in self.leaderboard.values():
            heapq.heappush(heap, num)
            if len(heap) > K:
                heapq.heappop(heap)
        while len(heap):
            res += heapq.heappop(heap)
        return res
    def reset(self, playerId: int) -> None:
        
        self.leaderboard[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)