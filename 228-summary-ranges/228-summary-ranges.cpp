class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) 
    {
        vector <string> ans;
        for(int start = 0; start < nums.size(); start++)
        {
            int end = start;
            while(end + 1 < nums.size() && nums[end+1] == nums[end] + 1)
                end++;
            if(end > start)
            {
                ans.push_back(to_string(nums[start]) + "->" + to_string(nums[end]));
            }
            else
            {
                ans.push_back(to_string(nums[start]));
            }
            start = end;
        }
        return ans;
    }
};