class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        outputs = []
        
        def backtrack(k, index, subSet):
            
            if index == k:
                
                outputs.append(subSet[:])
                
                return
            
            for i in range(index, len(nums)):
                
                backtrack(k, i + 1, subSet + [nums[i]])
                
        for j in range(len(nums) + 1):
            backtrack(j, 0, [])
        return outputs