class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n, m = len(sentence1), len(sentence2)
        if n!=m:
            return False
        dic = defaultdict(set)
        for s1, s2 in similarPairs:
            dic[s1].add(s2)
            dic[s2].add(s1)
        for s1, s2 in zip(sentence1, sentence2):
            if s1 == s2:
                continue
            if s1 in dic[s2]:
                    continue
            else:
                return False
        return True
            
        