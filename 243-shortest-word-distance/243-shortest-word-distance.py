class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        ans = first = second = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                first = i
            elif word == word2:
                second = i
            ans = min(abs(first - second), ans)
        return ans