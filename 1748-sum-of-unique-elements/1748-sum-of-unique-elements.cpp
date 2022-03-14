class Solution {
public:
    int sumOfUnique(vector<int>& nums) 
    {
        unordered_map <int, int> mp;
        for(auto c : nums)
        {
            mp[c]++;
        }
        int sum = 0;
        for(auto c : nums)
        {
            if(mp[c] == 1)
                sum += c;
        }
        return sum;
    }
};