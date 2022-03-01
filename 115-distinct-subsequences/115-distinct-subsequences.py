class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m, n = len(s), len(t)
        
        @lru_cache(None)
        def backtrack(i, j):
            if j >= n:
                return 1
            if i >= m:
                return 0
            count = 0
            if s[i] == t[j]:
                count += backtrack(i+1, j+1) +  backtrack(i+1, j) 
            else:
                count = backtrack(i+1, j)
            return count
        
        return backtrack(0, 0)
        