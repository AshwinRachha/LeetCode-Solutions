class Solution {
public:
    int findShortestSubArray(vector<int>& nums) 
    {
        unordered_map <int, vector<int>> map;
        
        for(int i = 0; i < nums.size(); i++)
        {
            map[nums[i]].push_back(i);
        }
        
        int count = 0;
        for(auto it : map)
        {
            count = max({count, (int)it.second.size()});
        }
        int degree = nums.size();
        
        for(auto it : map)
        {
            if(it.second.size() == count)
            {
                degree = min(degree, it.second[it.second.size()-1] - it.second[0] + 1);
            }
        }
        
        return degree;
    }
};