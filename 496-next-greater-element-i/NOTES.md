class Solution {
public:
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2)
{
stack <int> st;
map <int, int> mp;
for(auto c : nums2)
{
while(!st.empty() && st.top() < c)
{
mp[st.top()] = c;
st.pop();
}
st.push(c);
}
vector <int> ans(nums1.size(), -1);
int i = 0;
for(auto c: nums1)
{
if(mp.find(c) != mp.end())
{
ans[i] = mp[c];
}
i++;
}
return ans;
}
};