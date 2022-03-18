class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) 
    {
        vector <vector <int>> dp(triangle.size()+1, vector <int> (triangle.back().size()+1, 0));
        int rows = dp.size(); int cols = dp[0].size();
        
        for(int i = rows - 2; i >=0; i--)
        {
            for(int j = 0; j < i+1; j++)
            {
                dp[i][j] = triangle[i][j] + min({dp[i+1][j] , dp[i+1][j+1]});
            }
        }
        
        return dp[0][0];
    }
};