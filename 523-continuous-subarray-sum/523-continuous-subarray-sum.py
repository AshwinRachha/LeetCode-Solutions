class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = 0
        dic = {0 : 0}
        for i, num in enumerate(nums):
            prefix += num
            if prefix % k not in dic:
                dic[prefix % k] = i + 1
            elif dic[prefix % k] < i:
                return True
        return False
        