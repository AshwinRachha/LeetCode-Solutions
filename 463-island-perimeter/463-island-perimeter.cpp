class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) 
    {
        /*
         This proble can be solved in O(n^2) by simple counting. 
         We go through each cell
         If the cell is a water based cell, we ignore it
         If the cell is a ground based cell, then we check all the four sides of the cell.
         If the r-1  < 0 or c - 1 < 0 or r + 1 > rows or c + 1 > cols 
         If r-1 >= 0 and grid[r-1][c] == 0 then also we add a 1
        */
        
        int m = grid.size(); //row
        int n = grid[0].size(); //column
        int ans =0;
        for(int i =0;i<m;i++)
        {
            for(int j = 0;j<n;j++)
            {
                if(grid[i][j] == 1)
                { ans+=4; 
                     
                 
                   if( i+1 <m  && grid[i+1][j] == 1  )  // if down neighbour is there
                   {        ans--;}
                 if(   i-1 >=0 && grid[i-1][j] == 1 ) // if upward neighbour is there
                 { ans--;}
                   if(   j-1>=0  && grid[i][j-1] == 1)  // if left neighbour is there
                   {     ans--;}
                 if(  j+1<n && grid[i][j+1] == 1 ) // if right neighbour is there
                 { ans--;}
                }
            }
        }
        return ans;
        
    }
};