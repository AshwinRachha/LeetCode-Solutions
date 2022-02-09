class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        @lru_cache(maxsize = None)
        def backtrack(s, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start : end] in wordDict and backtrack(s, end):
                    return True
            return False
        return backtrack(s, 0)
        