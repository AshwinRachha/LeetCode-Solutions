class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) 
    {
        stack <int> st;
        int ans = 0;
        st.push(INT_MAX);
        for( auto num : arr)
        {
            while(!st.empty() && st.top()<=num)
            {
                int curr = st.top(); st.pop();
                ans += curr * min(st.top(), num);
            }
            st.push(num);
        }
        
        while(st.size() > 2)
        {
            int num1 = st.top(); st.pop(); 
            ans += num1 * st.top();
        }
        
        return ans;
    }
};