class Solution {
public:
    int calPoints(vector<string>& ops) 
    {
        stack <int> st;
        int ans = 0;
        for(auto c : ops)
        {
            if(c == "+")
            {
                int num1 = st.top(); st.pop();
                int num2 = st.top();
                st.push(num1);
                st.push(num1 + num2);
            }
            else if(c == "C")
            {
                st.pop();
            }
            else if(c == "D")
            {
                st.push(st.top() * 2);
            }
            else
            {
                st.push(stoi(c));
            }
        }
        while(!st.empty())
            {ans += st.top(); st.pop();}
        return ans;
    }
};