class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {0 : 1}
        
        prefixSum = 0
        
        ans = 0
        
        for num in nums:
            prefixSum += num
            if prefixSum - k in dic:
                ans += dic[prefixSum - k]
            dic[prefixSum] = dic.get(prefixSum, 0) + 1
        return ans
        
        1, 2, 3
        
        1, 3, 6
        