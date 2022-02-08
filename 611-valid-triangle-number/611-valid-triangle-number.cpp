class Solution {
public:
    int triangleNumber(vector<int>& nums) 
    {
        int count = 0;
        sort(nums.begin(), nums.end());
        for(int k = 2; k < nums.size(); k++)
        {
            int i = 0; int j = k - 1;
            while( i < j)
            {
                if(nums[i] + nums[j] > nums[k])
            {
                count += j - i;
                j -= 1;
            }
            else
                i+=1;
            }
        }
        return count;
    }
};