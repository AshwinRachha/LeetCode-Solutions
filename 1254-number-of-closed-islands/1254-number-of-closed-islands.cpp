class Solution {
public:
    
    void dfs(vector <vector<int>>& grid, int r, int c)
    {
        if(r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] != 0)
            return;
        grid[r][c] = -1;
        dfs(grid, r+1, c);
        dfs(grid, r-1, c);
        dfs(grid, r, c+1);
        dfs(grid, r, c-1);
    }
    
    int closedIsland(vector<vector<int>>& grid) {
        
        int rows = grid.size(); int cols = grid[0].size();
        int count = 0;
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if((r == 0 || c == 0 || r == rows-1 || c == cols - 1) && grid[r][c] == 0)
                    dfs(grid, r, c);
            }
        }
            
        
            
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid[r][c] == 0)
                {
                    dfs(grid, r, c);
                    count++;
                }
            }
        }
        
        return count;
    }
};