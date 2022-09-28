class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def PalindromeLength(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right += 1
            return right - left - 1
        start, end = 0, 0
        maxLength = float('-inf')
        for i in range(len(s)):
            len1 = PalindromeLength(s, i, i)
            len2 = PalindromeLength(s, i, i+1)
            maxLength = max(len1, len2)
            if maxLength > end - start:
                start = i - (maxLength - 1) // 2
                end = i + maxLength // 2
        return s[start : end + 1]