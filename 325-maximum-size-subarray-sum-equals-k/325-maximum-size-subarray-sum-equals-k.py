class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # 1, 0, 5, 3, 3
        dic = {0 : -1}
        prefixSum = 0
        ans = 0
        for i , num in enumerate(nums):
            prefixSum += num
            if (prefixSum - k) in dic:
                ans = max(ans, i - dic[prefixSum - k])
            dic[prefixSum] = dic.get(prefixSum, i)
        return ans