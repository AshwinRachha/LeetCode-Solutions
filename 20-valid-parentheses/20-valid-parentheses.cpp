class Solution {
public:
    bool isValid(string s) 
    {
        stack <char> st;
        unordered_map <char, char> mp;
        mp['}'] = '{';
        mp[']'] = '[';
        mp[')'] = '(';
        
        for(auto c : s)
        {
            if(!st.empty())
            {
                if(c == ')' || c == ']' || c == '}')
                {
                    if(st.top() == mp[c])
                        st.pop();
                    else
                        return false;
                }
                else
                    st.push(c);
            }
            else
                st.push(c);
        }
        
        return st.empty();
        
    }
};