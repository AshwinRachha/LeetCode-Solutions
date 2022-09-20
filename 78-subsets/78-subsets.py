class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        outputs = []
        n = len(nums)
        def backtrack(index, k, path):
            if len(path[:]) == k:
                outputs.append(path[:])
            for i in range(index, n):
                path.append(nums[i])
                backtrack(i + 1, k, path)
                path.pop()

        for k in range(n+1):
            backtrack(0, k, [])
        return outputs