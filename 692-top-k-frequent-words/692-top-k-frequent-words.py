class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        c = Counter(words)
        # dic = {}; for word in words: dic[word] = dic.get(word, 0) + 1
        ans = []
        for key, value in c.most_common():
            ans.append(key)
            k-=1
            if k == 0:
                break
        return ans