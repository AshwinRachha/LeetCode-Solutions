class Solution {
public:
    //dfs travel along row and column and just turn 1 into 0
    void dfs(vector<vector<int>>& grid, int r ,int c, int& count)
    {
        if(grid[r][c] == 1)
        {
            count++;
            grid[r][c] = 0;
            for(int i = 0; i < grid.size(); i++)
            {
                if(grid[i][c] == 1)
                    dfs(grid, i, c, count);
            }
            for(int j = 0; j < grid[0].size(); j++)
            {
                if(grid[r][j] == 1)
                    dfs(grid, r, j, count);
            }
        }
    }
    int countServers(vector<vector<int>>& grid) 
    {
        int ans=0;
        for(int r=0;r<grid.size();r++){
            for(int c=0;c<grid[0].size();c++)
            {
                if(grid[r][c]==1)
                {
                    int count=0;
                    dfs(grid,r,c,count);
                    if(count>1) ans+=count;
                }
            }
        }
        return ans;
    }
};