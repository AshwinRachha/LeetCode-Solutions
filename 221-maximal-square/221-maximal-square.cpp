class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) 
    {
        int max_square = 0;
        int n = matrix.size(), m = matrix[0].size();
        //cout<<m<<endl<<n;
        vector <vector <int>> dp(n + 1, vector <int>(m + 1, 0));
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <=m; j++)
            {
                if(matrix[i-1][j-1] == '1')
                {
                    dp[i][j] = min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]}) + 1;
                    max_square = max(max_square, dp[i][j]);
                }
            }
        }
        
        return max_square * max_square;
    }
};