class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        i = 0
        res = 0
        for c in columnTitle[::-1]:
            value = (ord(c) - ord('A')) + 1
            res += 26**i * value
            i+=1
        return res