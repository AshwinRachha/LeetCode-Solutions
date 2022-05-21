class Solution:
    def permuteUnique(self, nums):
        res, visited = [], [False]*len(nums)
        nums.sort()
        def dfs(nums, visited, path):
            if len(nums) == len(path):
                res.append(path)
                return 
            for i in range(len(nums)):
                if not visited[i]: 
                    if i>0 and not visited[i-1] and nums[i] == nums[i-1]: 
                        continue
                    visited[i] = True
                    dfs(nums, visited, path+[nums[i]])
                    visited[i] = False
        dfs(nums, visited, [])
        return res
    
        