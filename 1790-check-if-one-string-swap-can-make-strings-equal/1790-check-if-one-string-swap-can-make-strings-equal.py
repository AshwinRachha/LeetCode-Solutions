class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        count = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                count += 1
        if (count==2 or count==0) and sorted(s1)==sorted(s2):
            return True
        return False