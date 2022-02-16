class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        output = []
        def backtrack(path, index, target):
            if target == 0:
                output.append(path[:])
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target: break
                backtrack(path + [candidates[i]] , i+1,  target - candidates[i])

        
        backtrack([], 0, target)
        return output
            
        
                
                    