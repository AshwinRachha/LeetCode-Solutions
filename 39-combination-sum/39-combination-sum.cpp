class Solution {
public:
    
    void dfs(vector<vector<int>> &ans, vector<int> &path, int target, vector<int> &candidates, int index)
    {
        if(index == candidates.size())
        {
            if(target == 0)
            {
                ans.push_back(path);
                return;
            }
        }
        else
        {
             if(candidates[index] <= target)
                {
            path.push_back(candidates[index]);
            dfs(ans, path, target - candidates[index], candidates, index);
            path.pop_back();
                }
        dfs(ans, path, target, candidates, index+1);
        }
       
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) 
    {
        vector<vector<int>> ans;
        vector<int> path;
        dfs(ans, path, target, candidates, 0);
        return ans;
    }
};