class HitCounter:

    def __init__(self):
        
        self.dic = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        
        self.dic[timestamp] += 1
        
    def getHits(self, timestamp: int) -> int:
        res = 0
        for time in self.dic:
            if time > timestamp - 300:
                res += self.dic[time]
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)