class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) 
    {
        stack <int> st;
        int index = 0;
        for(int c : pushed)
        {
            st.push(c);
            while(index < popped.size() && !st.empty() && st.top() == popped[index])
            {
                st.pop();
                index++;
            }
        }
        
        return st.empty();
    }
};