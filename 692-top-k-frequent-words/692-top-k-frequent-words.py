class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        words.sort()
        count = sorted(Counter(words).items(), key = lambda x : x[1], reverse = True)
        #print(count)
        return [val for val, c in count[:k]]