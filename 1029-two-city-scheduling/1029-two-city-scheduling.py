class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x : x[0] - x[1])
        n = len(costs)
        ans = 0
        for i, x in enumerate(costs):
            if i < n // 2:
                ans += x[0]
            else:
                ans += x[1]
        return ans