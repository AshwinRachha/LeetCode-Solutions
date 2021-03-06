class Solution {
public:
    int triangleNumber(vector<int>& nums) 
    {
        sort(nums.begin(), nums.end());
        int ans = 0;
        for(int k = 2; k < nums.size(); k++)
        {
            int i = 0; int j = k - 1;
            while(i < j)
            {
                if(nums[i] + nums[j] > nums[k])
                {
                    ans += j - i;
                    j-=1;
                }
                else
                    i++;
            }
        }
        return ans;
    }
};