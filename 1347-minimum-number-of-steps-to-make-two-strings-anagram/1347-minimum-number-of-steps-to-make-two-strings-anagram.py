class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        ans = 0
        c1, c2 = Counter(s), Counter(t)
        print(c1, c2)
        for c in set(s + t):
            if c2[c] < c1[c]:
                ans += c1[c] - c2[c]
        return ans