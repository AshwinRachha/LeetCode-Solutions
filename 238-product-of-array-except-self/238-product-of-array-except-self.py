class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = 1
        prods = []
        for num in nums:
            prods.append(p)
            p = num * p
        #print(prods)
        p = 1
        for i in range(len(nums)-1, -1, -1):
            prods[i] *= p 
            p*=nums[i]
        return prods
        