class Solution {
public:
    
    void backtrack(vector<int>& grid, vector<int>& path, vector<vector<int>>& output, int target, int index, int s)
    {
        if(s == target)
        {
            output.push_back(path);
            return;
        }
        for(int i = index; i < grid.size(); i++)
        {
            if(i > index && grid[i] == grid[i-1])
                continue;
            if(s + grid[i] > target)
                continue;
            path.push_back(grid[i]);
            backtrack(grid, path, output, target, i + 1, s + grid[i]);
            path.pop_back();
        }
            
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) 
    {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        vector <vector<int>> output;
        backtrack(candidates, path, output, target, 0, 0);
        return output;
    }
};