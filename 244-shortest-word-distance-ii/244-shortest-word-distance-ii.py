class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        self.dic = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.dic[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        
        distance = float('inf')
        i, j = 0, 0
        while i < len(self.dic[word1]) and j < len(self.dic[word2]):
            distance = min(distance, abs(self.dic[word1][i] - self.dic[word2][j]))
            if self.dic[word1][i] < self.dic[word2][j]:
                i += 1
            else:
                j += 1
        return distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)