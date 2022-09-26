class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])
        #print(timestamp)
        timestamp.sort()
        #print(timestamp)
        used_cap = 0
        for time, passanger_change in timestamp:
            used_cap += passanger_change
            if used_cap > capacity:
                return False
        return True
                