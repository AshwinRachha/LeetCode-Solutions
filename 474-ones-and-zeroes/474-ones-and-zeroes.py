class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        counter = [[s.count("0"), s.count("1")] for s in strs]
        
        @lru_cache(maxsize = None)
        def dp(i, j, index):
            if i < 0 or j < 0:
                return float('-inf')
            if index == len(strs):
                return 0
            return max(dp(i,j,index+1), 1 + dp(i-counter[index][0], j-counter[index][1], index+1))
        return dp(m, n, 0)        