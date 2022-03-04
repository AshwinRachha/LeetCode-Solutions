class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) 
    {
        int i = 0, j = 0, k = 0;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int count = 0;
        while(i < n - 2)
        {
            j = i + 1;
            k = n - 1;
            while(j < k)
            {
                int sum = nums[i] + nums[j] + nums[k];
                if(sum >= target)
                    k-=1;
                else
                {
                    count += k - j;
                    j+=1;
                }
            }
            i++;
        }
        
        return count;
    }
};