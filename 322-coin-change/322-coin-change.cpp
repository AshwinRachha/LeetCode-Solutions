class Solution {
public:
    int coinChange(vector<int>& coins, int amount) 
    {
        vector <int> dp(amount+1, INT_MAX / 2);
        dp[0] = 0;
        for(auto coin : coins)
        {
            for(int i = 1; i < amount + 1; i++)
            {
                if(i >= coin)
                {
                    dp[i] = min(dp[i], 1 + dp[i-coin]);
                }
            }
        }
        
        return dp[amount] == INT_MAX/2 ? -1 : dp[amount];
    }
};