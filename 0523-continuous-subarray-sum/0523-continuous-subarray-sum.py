class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        """
        2 + 4 = 6 Y
        6 N
        1. Brute Force (Straightforward) 
        Iterate over each subarray, find the sum and find if the subarray sum is divisible by k.
        
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s +=  nums[j]
                if j - i + 1 >= 2 and s % k == 0:
                    return True
        return False
        
        2. 
        
        """
        
        dic = {0 : -1}
        prefixSum = 0
        for i, num in enumerate(nums):
            prefixSum = (prefixSum + num) % k
            if prefixSum not in dic:
                dic[prefixSum] = i
            else:
                if  i - dic[prefixSum] > 1:
                    return True
        return False
            
        
        