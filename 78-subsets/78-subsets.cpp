class Solution {
public:
    
    void backtrack(vector <int> &nums, vector<int> &path, vector<vector<int>> &ans, int index, int k)
    {
        if(path.size() == k)
        {
            ans.push_back(path);
            return;
        }
        for(int j = index; j < nums.size(); j++)
        {
            path.push_back(nums[j]);
            backtrack(nums, path,  ans, j+1, k);
            path.pop_back();
        }
    }
    
    vector<vector<int>> subsets(vector<int>& nums) 
    {
        vector<vector <int>> ans;
        vector <int> path;
        for(int k = 0; k < nums.size() + 1; k++)
        {
            backtrack(nums, path, ans, 0, k);
        }
        return ans;
    }
};