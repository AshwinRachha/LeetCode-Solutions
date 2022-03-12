class Solution {
public:
    void dfs(vector <vector <int>>& grid, int rows, int cols, int r, int c)
    {
        if(r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0)
            return;
        grid[r][c] = 0;
        dfs(grid, rows,cols, r + 1 ,c);
        dfs(grid, rows,cols, r - 1 ,c);
        dfs(grid, rows,cols, r,c + 1);
        dfs(grid, rows,cols, r,c - 1);
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) 
    {
        int rows = grid1.size(); int cols = grid1[0].size();
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid1[r][c] == 0 && grid2[r][c] == 1)
                    dfs(grid2, rows, cols, r, c);
            }
        }
        int count = 0;
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid2[r][c] == 1)
                {
                    dfs(grid2, rows, cols, r, c);
                    count++;
                }
            }
        }
        return count;
    }
};