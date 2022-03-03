class Solution {
public:
    
    void backtrack(vector <vector<char>>& grid, int r, int c, int rows, int cols)
    {
        if(r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == '0')
            return;
        grid[r][c] = '0';
        backtrack(grid, r-1, c, rows, cols);
        backtrack(grid, r+1, c, rows, cols);
        backtrack(grid, r, c + 1, rows, cols);
        backtrack(grid, r, c - 1, rows, cols);
        
    }
    
    int numIslands(vector<vector<char>>& grid) 
    {
        int count = 0;
        int rows = grid.size(); int cols = grid[0].size();
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid[r][c] == '1')
                {
                    count++;
                    backtrack(grid, r, c, rows, cols);
                }
            }
        }
        
        return count;
    }
};