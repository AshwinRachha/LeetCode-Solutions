class Solution {
public:
    //dfs travel along row and column and just turn 1 into 0
    void dfs(vector<vector<int>>& grid, int i ,int j, int &count){
        if(grid[i][j]==1){
            count++;
            grid[i][j]=0;
            for(int c=0;c<grid[0].size();c++){
                if(grid[i][c]==1)dfs(grid,i,c,count);
            }
            for(int r=0;r<grid.size();r++){
                if(grid[r][j]==1)dfs(grid,r,j,count);
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