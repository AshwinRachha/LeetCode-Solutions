class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def backtrack(path, index, k):
            if len(path) == k:
                output.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1, k)
                path.pop()
        for k in range(len(nums) + 1):
            backtrack([], 0, k)
        return output