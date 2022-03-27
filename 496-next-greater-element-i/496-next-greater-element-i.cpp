class Solution {
public:
    
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) 
    {
        stack <int> st;
        map <int, int> mp;
        for(int i : nums2)
        {
            while(!st.empty() && st.top() < i)
            {
                mp[st.top()] = i;
                st.pop();
            }
            st.push(i);
        }
            vector <int> ans;
            for(int j = 0; j < nums1.size(); j++)
            {
                if(mp.find(nums1[j])!=mp.end())
                    ans.push_back(mp[nums1[j]]);
                else
                    ans.push_back(-1);
            }
        return ans;
    }
};