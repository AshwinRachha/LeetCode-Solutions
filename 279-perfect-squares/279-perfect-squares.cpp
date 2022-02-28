class Solution {
public:
    int numSquares(int n) 
    {
        vector <int> dp(n+1,n+1);
        dp[0] = 0;
        for(int target = 1; target <= n; target++)
        {
            for(int s = 1; s <= target; s++)
            {
                int squared = s * s;
                if(target - squared < 0)
                    break;
                dp[target] = min(dp[target], 1 + dp[target -squared]);
            }
        }
    
        return dp[n];
    }
};