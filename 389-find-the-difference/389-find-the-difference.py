class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        for l in t:
            if l not in c or c[l] == 0:
                return l
            c[l]-=1