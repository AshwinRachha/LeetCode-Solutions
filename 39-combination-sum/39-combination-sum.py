class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        outputs = []
        def backtrack(index, path, s):
            if index >= len(candidates):
                if s == target:
                    outputs.append(path[:])
                return
            elif s + candidates[index] <= target:
                path.append(candidates[index])
                backtrack(index, path, s + candidates[index])
                path.pop()
            backtrack(index+1, path, s)
        
        backtrack(0, [], 0)
        return outputs
        