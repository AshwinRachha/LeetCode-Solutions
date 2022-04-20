class Solution {
public:
    int totalGold = 0;
    void depthFirstSearch(vector <vector<int>> &grid, int r, int c, int rows, int cols, int goldCollected)
    {
        if(r < 0 || c < 0 || r >= rows  || c >= cols || grid[r][c] == 0)
            return;
        int tempGold = grid[r][c];
        grid[r][c] = 0;
        totalGold = max(totalGold, goldCollected + tempGold);
        depthFirstSearch(grid, r + 1, c, rows, cols, goldCollected + tempGold);
        depthFirstSearch(grid, r - 1, c, rows, cols, goldCollected + tempGold);
        depthFirstSearch(grid, r, c + 1, rows, cols, goldCollected + tempGold);
        depthFirstSearch(grid, r, c - 1, rows, cols, goldCollected + tempGold);
        grid[r][c] = tempGold;
        
    }
    
    int getMaximumGold(vector<vector<int>>& grid) 
    {
        int rows = grid.size(); int cols = grid[0].size();
        
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid[r][c]!=0)
                    depthFirstSearch(grid, r, c, rows, cols, 0);
            }
        }
        return totalGold;
    }
};