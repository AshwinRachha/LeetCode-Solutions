class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closest = float('inf')
        i = 0
        nums.sort()
        while i < len(nums):
            j = i+1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    j+=1
                else:
                    k-=1
            i+=1
        return closest