class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix)
    {
        int rows = matrix.size(); int cols = matrix[0].size();
        for(int r = rows - 2; r >= 0; r--)
        {
            for(int c = 0; c < cols; c++)
            {
                if(c == 0)
                    matrix[r][c] += min(matrix[r+1][c], matrix[r+1][c+1]);
                else if(c == cols-1)
                    matrix[r][c] += min(matrix[r+1][c] , matrix[r+1][c-1]);
                else
                    matrix[r][c] += min({matrix[r+1][c-1] , matrix[r+1][c] , matrix[r+1][c+1]});
            }
        }
        
        int minSum = INT_MAX;
        for(auto sum : matrix[0])
            minSum = min(minSum, sum);
        return minSum;
    }
};