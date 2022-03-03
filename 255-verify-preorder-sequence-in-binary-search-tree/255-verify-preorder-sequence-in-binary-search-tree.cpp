class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) 
    {
        //In BST only one dip allowed
        //If two dips, then return false
        
        int check = INT_MIN;
        
        stack <int> st;
        
        for(auto c : preorder)
        {
            while(!st.empty() && st.top() < c)
            {
                check = st.top();
                st.pop();
            }
            if(check != INT_MIN && check > c)
                return false;
            st.push(c);
        }
        
        return true;
        
    }
};