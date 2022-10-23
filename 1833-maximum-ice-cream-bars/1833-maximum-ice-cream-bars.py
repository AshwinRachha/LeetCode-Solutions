class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        ans = 0
        spent = 0
        for c in costs:
            if spent + c <= coins:
                spent += c
                ans += 1
            if spent == coins:
                return ans 
        return ans
        