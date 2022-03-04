class Solution {
public:
    
    void backtrack(vector<int>& nums, int index, vector<int>& path, vector<vector<int>>& output)
    {
        output.push_back(path);
        for(int i = index; i < nums.size(); i++)
        {
            if(i!=index && nums[i] == nums[i-1])
                continue;
            path.push_back(nums[i]);
            backtrack(nums, i+1, path, output);
            path.pop_back();
        }
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) 
    {
        vector<vector<int>> output;
        vector <int> ans;
        sort(nums.begin(), nums.end());
        backtrack(nums, 0, ans, output);
        return output;
        
    }
};