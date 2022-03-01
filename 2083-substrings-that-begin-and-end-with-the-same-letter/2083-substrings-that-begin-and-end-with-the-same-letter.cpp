class Solution {
public:
    long long numberOfSubstrings(string s) 
    {
        unordered_map <char, int> mp;
        long long ans = 0;
        for(auto c : s)
        {
            mp[c]++;
            ans += mp[c];
        }
        return ans;
        
    }
};