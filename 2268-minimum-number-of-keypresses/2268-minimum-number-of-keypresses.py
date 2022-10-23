class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        ans = 0
        c = sorted(Counter(s).values(), reverse = True)
        cnt = 0
        for i, elem in enumerate(c):
            if i % 9 == 0:
                cnt += 1
            ans += cnt * elem
        return ans
        
        