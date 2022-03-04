class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) 
    {
        int rows = mat.size(); int cols = mat[0].size();
        if(rows == 0 || rows * cols != r * c)
            return mat;
        deque <int> q;
        for(int i = 0; i < rows; i++)
            for(int j = 0; j < cols; j++)
                q.push_back(mat[i][j]);
        vector <vector<int>> ans(r, vector <int>(c, 0));
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
            {
                ans[i][j] = q.front();
                q.pop_front();
            }
        
        return ans;
        
    }
};