class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount+1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1