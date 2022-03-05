class Solution {
public:
    
    void dfs(vector <vector<int>>& image, int rows, int cols, int r, int c, int newColor, int oldColor)
    {
        if(r < 0 || r >= rows || c < 0 || c >= cols || image[r][c] !=oldColor || image[r][c] == newColor)
            return;
        image[r][c] = newColor;
        dfs(image, rows, cols, r+1, c, newColor, oldColor);
        dfs(image, rows, cols, r-1, c, newColor, oldColor);
        dfs(image, rows, cols, r, c+1, newColor, oldColor);
        dfs(image, rows, cols, r, c-1, newColor, oldColor);
    }
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) 
    {
        int rows = image.size(); int cols = image[0].size();
        int oldColor = image[sr][sc];
        dfs(image, rows, cols, sr, sc, newColor, oldColor);
        return image;
        
    }
};