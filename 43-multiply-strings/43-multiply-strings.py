class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def to_int(string):
            result = 0
            for c in string:
                result = 10*result + ( ord(c) - ord('0'))
            return result
        
        def to_string(integer):
            result = ''
            if integer == 0:
                return '0'
            while integer>0:
                remainder = integer % 10
                integer //= 10
                result += chr(ord('1') + remainder - 1)
            return result[::-1]
        
        result = to_int(num1) * to_int(num2)
        
        return to_string(result)
        