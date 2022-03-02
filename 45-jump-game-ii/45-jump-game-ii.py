class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i, jumps, lastPos, maxPos = 0, 0, 0, 0
        n = len(nums)
        while i < n - 1:
            
            maxPos = max(maxPos, i + nums[i])
            if i == lastPos:
                lastPos = maxPos
                jumps+=1
            i+=1
        return jumps
        