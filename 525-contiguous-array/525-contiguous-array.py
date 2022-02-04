class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
                
        dic = {0 : -1}
        prefixSum = 0
        maximum = 0
        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum in dic:
                maximum = max(maximum, i - dic[prefixSum])
            else:
                dic[prefixSum] = i
        return maximum