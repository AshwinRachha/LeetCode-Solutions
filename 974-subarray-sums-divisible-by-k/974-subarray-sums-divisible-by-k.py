class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        dic = defaultdict(int)
        dic[0] = 1
        prefixSum = 0
        res = 0
        for num in nums:
            prefixSum += num
            prefixSum = prefixSum % k
            res += dic[prefixSum % k]
            dic[prefixSum % k] += 1
        return res
        