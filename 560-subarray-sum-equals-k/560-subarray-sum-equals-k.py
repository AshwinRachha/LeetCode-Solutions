class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {0 : 1}
        count = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            if prefixSum-k in dic:
                count += dic[prefixSum-k]
            dic[prefixSum] = dic.get(prefixSum, 0) + 1
        return count