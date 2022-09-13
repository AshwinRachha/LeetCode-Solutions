class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        clone = sorted(nums)
        start = len(nums); end = 0
        
        for i in range(len(clone)):
            if clone[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
        
        return end - start + 1 if end - start >= 0 else 0
        
        