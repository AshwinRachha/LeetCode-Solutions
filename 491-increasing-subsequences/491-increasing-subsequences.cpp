class Solution {
public:
    
    void backtrack(set <vector<int>>& st,int index, vector <int>& nums, vector <int>& curr, vector <vector<int>>& output, int val)
    {
        if (index == nums.size()+1)
            return;
        
        if (curr.size() > 1 and st.find(curr) == st.end()){
            output.push_back(curr);
            st.insert(curr);
        }
        for(int i = index; i < nums.size(); i++)
        {
            if(val <= nums[i])
            {
                curr.push_back(nums[i]);
                backtrack(st, i+1, nums, curr, output, nums[i]);
                curr.pop_back();
            }
           
        }
        
    }
    
    vector<vector<int>> findSubsequences(vector<int>& nums) 
    {
        set <vector<int>> st;
        vector <vector <int>> output;
        vector <int> curr;
        backtrack(st, 0, nums, curr, output, INT_MIN);
        return output;
    }
};