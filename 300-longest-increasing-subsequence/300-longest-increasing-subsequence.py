class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        i, j = 1, 0
        while i < n:
            j = i-1
            while j >= 0:
                if j >=0 and nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                j-=1
            i += 1
        return max(dp)