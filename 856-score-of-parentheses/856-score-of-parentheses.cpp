class Solution {
public:
    int scoreOfParentheses(string s) 
    {
        stack <int> st;
        st.push(0);
        for(char c : s)
        {
            if(c == '(')
                st.push(0);
            else
            {
                int num1 = st.top(); st.pop();
                int num2 = st.top(); st.pop();
                st.push(num2 + max({2*num1, 1}));
            }
        }
        return st.top();
    }
};