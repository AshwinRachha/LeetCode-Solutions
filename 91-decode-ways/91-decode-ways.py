class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @lru_cache(maxsize = None)
        def backtrack(index):
            if index == n:
                return 1
            if s[index] == '0':
                return 0
            if index == n - 1:
                return 1
            answer = backtrack(index + 1)
            if int(s[index : index + 2]) <= 26:
                answer += backtrack(index + 2,)
            return answer
        
        return backtrack(0)
            