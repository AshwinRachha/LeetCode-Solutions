class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        int max_len = 0;
        int start = 0;
        map <char, int> mp;
        for(int end = 0; end < s.size(); end++)
        {
            if(mp.find(s[end])!=mp.end() && mp[s[end]] >= start)
            {
                start = mp[s[end]] + 1;
            }
            mp[s[end]] = end;
            max_len = max(max_len, end - start + 1);
        }
        
        return max_len;
        
    }
};