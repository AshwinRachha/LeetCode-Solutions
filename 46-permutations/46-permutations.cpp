class Solution {
public:
    
    unordered_set <int> st;
    
    void backtrack(vector <int>& nums, vector <vector<int>>& ans, int index, vector <int> permute)
    {
        if(permute.size() == nums.size())
        {
            ans.push_back(permute);
            return;
        }
        for(int i = 0; i < nums.size(); i++)
        {
            if(st.find(i)==st.end())
            {
                st.insert(i);
                permute.push_back(nums[i]);
                backtrack(nums, ans, i+1, permute);
                permute.pop_back();
                st.erase(i);
            }
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) 
    {
        vector <int> permute;
        vector <vector <int>> ans;
        backtrack(nums, ans, 0, permute);
        return ans;
    }
};