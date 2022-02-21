class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                majority = num
            if num == majority:
                count+=1
            elif num!=majority:
                count-=1
            
        return majority