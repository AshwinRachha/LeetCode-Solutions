class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []
        n = len(nums)
        seen = set()
        def backtrack(index, k, curr):
            if index >= k:
                if tuple(curr) not in seen:
                    seen.add(tuple(curr[:]))
                    output.append(curr[:])
            else:
                for i in range(index, n):
                    curr.append(nums[i])
                    backtrack(i + 1, k, curr)
                    curr.pop()
        for k in range(n + 1):
            backtrack(0, k, [])
        return output
        