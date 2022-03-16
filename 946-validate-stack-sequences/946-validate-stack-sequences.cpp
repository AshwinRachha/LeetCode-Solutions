class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) 
    {
        stack <int> st;
        int index = 0;
        for(int num : pushed)
        {
            st.push(num);
            while(!st.empty() && index < popped.size() && popped[index] == st.top())
            {
                st.pop();
                index++;
            }
        }
        return st.empty();
    }
};