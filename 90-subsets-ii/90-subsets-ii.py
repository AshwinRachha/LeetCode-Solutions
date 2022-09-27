class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []
        n = len(nums)
        def backtrack(index, curr):
            output.append(curr[:])
            for i in range(index, n):
                if i != index and nums[i] == nums[i-1]:
                    continue
                else:
                    curr.append(nums[i])
                    backtrack(i + 1, curr)
                    curr.pop()
        backtrack(0, [])
        return output
        