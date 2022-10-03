class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def find(word):
            i = 0
            check, dic = "", {}
            for w in word:
                if w in dic:
                    check += "," + dic[w]
                else:
                    dic[w] = str(i)
                    check += "," + str(i)
                    i += 1
            return check
        
        c1 = find(pattern)
        ans = []
        for word in words:
            c2 = find(word)
            if c1 == c2:
                ans.append(word)
        return ans
        