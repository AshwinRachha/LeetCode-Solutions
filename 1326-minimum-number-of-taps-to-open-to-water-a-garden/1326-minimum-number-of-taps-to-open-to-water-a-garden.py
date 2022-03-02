class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(n + 1):
            intervals.append( [i-ranges[i], i + ranges[i]])
        intervals.sort(key = lambda x : x[0])
        
        start = ans = end = i = 0
        
        while start < n:
            while i <= n and intervals[i][0] <= start:
                end = max(end, intervals[i][1])
                i+=1
            if start == end:
                return -1
            start = end
            ans += 1
        return ans