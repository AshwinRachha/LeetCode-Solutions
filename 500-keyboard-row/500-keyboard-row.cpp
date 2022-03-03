class Solution {
public:
    vector<string> findWords(vector<string>& words) 
    {
        unordered_map <char, int> mp;
        int count = 0;
        vector <string> keyboard = {"qwertyuiop","asdfghjkl", "zxcvbnm"};
        for(auto w : keyboard)
        {
            for(auto c : w)
            {
                mp[c] = count;
            }
            count ++;
        }
        vector <string> ans;
        for(auto w : words)
        {
           int flag = 1;
           int check = mp[tolower(w[0])];
           for(auto c : w)
           {
               if(mp[tolower(c)] != check)
               {
                   flag = 0;
                   break;
               }
           }
            
            if(flag == 1)
                ans.push_back(w);
        }
        return ans;
        
    }
};