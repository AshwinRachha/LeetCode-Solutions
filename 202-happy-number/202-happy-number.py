class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        seen = set()
        
        def find_summed_squares(n):
            s = 0
            while n > 0:
                n, digit = divmod(n, 10)
                s += digit ** 2
            return s
        while n!=1 and n not in seen:
            seen.add(n)
            n = find_summed_squares(n)
        return n == 1
                
        