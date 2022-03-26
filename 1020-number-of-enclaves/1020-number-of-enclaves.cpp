class Solution {
public:
    
    int dfs(vector <vector <int>>& grid, int r, int c)
    {
        if(r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1 , c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1);
    }
    
    int numEnclaves(vector<vector<int>>& grid) 
    {
        int rows = grid.size(); int cols = grid[0].size();
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if((r == 0 || r == rows - 1 || c == 0 || c == cols - 1) && grid[r][c] == 1)
                    dfs(grid, r, c);
            }
        }
        int enclaves = 0;
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid[r][c] == 1)
                    enclaves += dfs(grid, r, c);
            }
        }
        
        return enclaves;
    }
};