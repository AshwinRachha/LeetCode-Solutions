class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        total_time, left,right = 0, 0, 0
        i,j, n = 0,0, len(colors)
        while i < n and j < n:
            curr_total = 0
            curr_max = 0
            while j < n and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
            total_time += curr_total - curr_max
            i = j
        return total_time