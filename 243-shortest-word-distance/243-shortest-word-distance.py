class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        dic = defaultdict(list)
        for i, word in enumerate(wordsDict):
            dic[word].append(i)
        distance = float('inf')
        i, j = 0, 0
        while i < len(dic[word1]) and j < len(dic[word2]):
            distance = min(distance, abs(dic[word1][i] - dic[word2][j]))
            if dic[word1][i] < dic[word2][j]:
                i += 1
            else:
                j += 1
        return distance