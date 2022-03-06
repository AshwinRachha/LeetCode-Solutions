class Solution {
public:
    
    int depthFirstSearch(vector <vector<int>>& grid, int r, int c)
    {
        if(r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        return 1 + depthFirstSearch(grid, r+1,c) + depthFirstSearch(grid, r-1,c) + depthFirstSearch(grid, r,c+1) + depthFirstSearch(grid, r,c-1);
    }
    
    int maxAreaOfIsland(vector<vector<int>>& grid) 
    {
        int max_area = 0;
        int rows = grid.size(); int cols = grid[0].size();
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid[r][c] == 1)
                    max_area = max(max_area, depthFirstSearch(grid,r,c));
            }
        }
        return max_area;
    }
};