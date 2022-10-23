class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        ans = 0
        start = 0
        count = sorted(Counter(s).values(), reverse = True)
        for i, frequency in enumerate(count):
            
            # If we are at an index that is the beginning or is overflowing the last 9th cell,
            # Then we start from the top.
            if i % 9 == 0:
                start += 1
            ans += start * frequency
        return ans
        
        