class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        power = len(columnTitle)-1
        result = 0
        for c in columnTitle:
            result += 26**power*(ord(c) - ord('A') + 1)
            power -= 1
        return result