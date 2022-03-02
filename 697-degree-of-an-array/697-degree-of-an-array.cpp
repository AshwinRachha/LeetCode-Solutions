class Solution {
public:
    int findShortestSubArray(vector<int>& nums) 
    {
        unordered_map <int, vector<int>> mp;
        
        for(int i = 0; i < nums.size(); i++)
        {
            mp[nums[i]].push_back(i);
        }
        
        int degree = 0;
        
        for(auto it : mp)
        {
            degree = max(degree,(int)it.second.size());
        }
        int count = nums.size();
        for(auto it : mp)
        {
            if(it.second.size() == degree)
            {
                count = min(count, it.second.back() - it.second[0] + 1);
            }
        }
        return count;
        
    }
};