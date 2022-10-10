class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""
        found_a = False
        palindrome = list(palindrome)
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a' and not found_a:
                palindrome[i] = 'a'
                return "".join(palindrome)
        palindrome[-1] = "b"
        return "".join(palindrome)
        