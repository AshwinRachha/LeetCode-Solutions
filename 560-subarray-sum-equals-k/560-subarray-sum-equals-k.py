class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {0 : 1}
        ans = 0
        prefixSum = 0
        for i, n in enumerate(nums):
            prefixSum += n
            if prefixSum - k in dic:
                ans += dic[prefixSum - k]
            dic[prefixSum] = dic.get(prefixSum, 0) + 1
        return ans

        