class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        def binary_search(left, right, number):
            if left > right:
                return False
            mid = (left + right) // 2
            if mid * mid == number:
                return True
            if mid * mid > number:
                return binary_search(left, mid - 1, number)
            return binary_search(mid + 1, right, number)
        
        a = 0
        while a * a <= c:
            b = c - a*a
            if binary_search(0, b, b): return True
            a += 1
        return False
            
            
        