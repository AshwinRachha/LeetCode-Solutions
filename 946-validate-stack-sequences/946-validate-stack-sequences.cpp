class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) 
    {
        int index = 0;
        stack <int> st;
        for(int i : pushed)
        {
            st.push(i);
            while(!st.empty()  && st.top() == popped[index])
            {
                st.pop();
                index++;
            }
        }
        return st.empty();
    }
};