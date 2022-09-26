class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum, longestSum = 0, float('-inf')
        for i, n in enumerate(nums):
            currSum = max(n, currSum + n)
            longestSum = max(longestSum, currSum)
        return longestSum