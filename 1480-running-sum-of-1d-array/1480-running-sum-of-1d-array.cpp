class Solution {
public:
    vector<int> runningSum(vector<int>& nums) 
    {
        int prev_num = nums[0];
        for(int i = 1; i < nums.size(); i++)
        {
            nums[i] += prev_num;
            prev_num = nums[i];
        }
        return nums;
    }
};