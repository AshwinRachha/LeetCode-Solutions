class Solution {
public:
    int minProductSum(vector<int>& nums1, vector<int>& nums2) 
    {
        sort(nums1.begin(), nums1.end());
        priority_queue <int, vector <int>> pq;
        for(int num : nums2)
            pq.push(num);
        int ans = 0;
        for(int idx = 0; idx < nums2.size(); idx++)
        {
            ans += nums1[idx] * pq.top();
            pq.pop();
        }
        return ans;
    }
};