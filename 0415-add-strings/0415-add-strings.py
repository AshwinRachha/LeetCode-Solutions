class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        """
        
        1. Use library functions to convert to integer, compute sum, convert to string
        
        return str(int(num1) + int(num2))
        
        2. Design Custom Function to do conversions mentioned above.
                
        3. Iterate through the strings and then add using elementary math
        
        
        """
        
        s, c = 0, 0
        
        n, m = len(num1) - 1, len(num2) - 1
        
        ans = ''
        
        while n >= 0 or m >= 0:
            
            if n >= 0:
                val1 = ord(num1[n]) - ord('0')
            else:
                val1 = 0
            
            if m >= 0:
                val2 = ord(num2[m]) - ord('0')
            else:
                val2 = 0
            #print(val1, val2)
            
            c, s = divmod(val1 + val2 + c, 10)
            ans += str(s)
            n -= 1
            m -= 1
        if c:
            ans += '1'
        return ans[::-1]
        
        
        
        