class Solution:
    def minDeletions(self, s: str) -> int:
        
        freqs = sorted(Counter(s).values(), reverse = True)
        ans = 0
        next_unused = len(s)
        for freq in freqs:
            next_unused = min(freq, next_unused)
            ans += freq - next_unused
            if next_unused > 0:
                next_unused -= 1
        return ans
        