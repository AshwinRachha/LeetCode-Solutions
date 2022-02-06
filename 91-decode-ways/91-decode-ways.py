class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(maxsize = None)
        def dfs(s, index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index == len(s)-1:
                return 1
            ans = dfs(s, index + 1)
            if int(s[index : index + 2]) <= 26:
                ans += dfs(s, index + 2)
            
            return ans
        
        return dfs(s, 0)
            