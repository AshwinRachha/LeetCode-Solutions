class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        n = len(s)
        @lru_cache(maxsize = None)
        def backtrack(index, s):
            if index == n:
                return True
            for i in range(index + 1, n + 1):
                if s[index : i] in wordDict and backtrack(i, s):
                    return True
            return False
        return backtrack(0, s)