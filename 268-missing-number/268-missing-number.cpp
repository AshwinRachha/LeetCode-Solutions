class Solution {
public:
    int missingNumber(vector<int>& nums) 
    {
        int n = nums.size();
        int expectedSum = (n * (n + 1) )/ 2;
        int actualSum = 0;
        for(auto c : nums)
            actualSum += c;
        return expectedSum - actualSum;
    }
};