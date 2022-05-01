class Solution {
public:
    
    string convert(string s)
    {
        stack <char> st;
        string compare = "";
        for(char c : s)
        {
            if(c != '#')
                st.push(c);
            else
                if(!st.empty())
                    st.pop();
        }
        while(!st.empty())
        {
            compare += st.top();
            st.pop();
        }
        return compare;
    }
    
    bool backspaceCompare(string s, string t) 
    {
        return convert(s) == convert(t);
    }
};