class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        c = Counter(magazine)
        
        for ch in ransomNote:
            if c[ch] <= 0:
                return False
            else:
                c[ch]-=1
        return True
            
        