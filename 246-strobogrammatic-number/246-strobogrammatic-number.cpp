class Solution {
public:
    bool isStrobogrammatic(string num) 
    {
        unordered_map <char, char> mp;
        mp['0'] = '0';
        mp['1'] = '1';
        mp['8'] = '8';
        mp['6'] = '9';
        mp['9'] = '6';
        string ans = "";
        for(auto c : num)
        {
            if(mp.find(c)==mp.end())
                return false;
            else
                ans += mp[c];
        }
        string temp = "";
        for(int i = ans.size() - 1; i >= 0; i--)
            temp += ans[i];
        return temp == num;
    }
};