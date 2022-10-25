class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        sums = [0] * n
        sums[0] = nums[0]
        
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]
        res = sums[k-1] / k
        for i in range(k, n):
            res = max(res, (sums[i] - sums[i-k])/k)
        return res