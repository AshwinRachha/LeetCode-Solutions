class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def backtrack(index, path, target):
            if index >= len(candidates):
                if target == 0:
                    output.append(path[:])
                return
            else:
                if target - candidates[index] >= 0:
                    backtrack(index, path + [candidates[index]], target - candidates[index])
                backtrack(index + 1, path, target)
                
        backtrack(0, [], target)
        return output