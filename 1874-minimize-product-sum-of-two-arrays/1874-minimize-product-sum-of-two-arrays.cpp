class Solution {
public:
    int minProductSum(vector<int>& nums1, vector<int>& nums2) 
    {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end(), greater <int>());
        int product = 0;
        for(int i = 0; i < nums2.size(); i++)
        {
            product += nums1[i] * nums2[i]; 
        }
        return product;
    }
};