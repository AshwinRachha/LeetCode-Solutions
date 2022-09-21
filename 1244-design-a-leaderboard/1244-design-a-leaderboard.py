class Leaderboard:

    def __init__(self):
        
        self.leaderboard = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        
        self.leaderboard[playerId] += score

    def top(self, K: int) -> int:
        
        return sum( l[1] for l in self.leaderboard.most_common(K))
    
    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)