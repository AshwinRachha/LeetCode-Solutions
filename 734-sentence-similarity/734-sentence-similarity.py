class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        n = len(sentence1)
        graph = defaultdict(set)
        for word1, word2 in similarPairs:
            if word2 not in graph[word1]: graph[word1].add(word2)
            if word1 not in graph[word2]:  graph[word2].add(word1)
            
        for i in range(n):
            if sentence1[i] == sentence2[i]:
                continue
            elif sentence1[i] in graph[sentence2[i]]:
                continue
            else:
                return False
        return True
            