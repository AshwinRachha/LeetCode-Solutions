class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        dic = dict()
        num = 0
        for l in ["qwertyuiop", "asdfghjkl", "zxcvbnm" ]:
            for c in l:
                dic[c] = num
            num += 1
        ans = []
        for word in words:
            check = dic[word[0].lower()]
            to_add = True
            for c in word:
                if dic[c.lower()] != check:
                    to_add = False
                    break
            if to_add:
                ans.append(word)
        return ans