class Solution {
public:
    int subarraySum(vector<int>& nums, int k) 
    {
        int temp[20000000] = {0};
        int count =0, prefixSum = 0;
        temp[10000000] = 1;
        for(int i = 0; i < nums.size(); i++)
        {
            prefixSum += nums[i];
            count += temp[prefixSum - k +10000000];
            temp[prefixSum + 10000000] += 1;
        }
        return count;
    }
};