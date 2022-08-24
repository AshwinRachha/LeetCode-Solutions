class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        outputs = []
        
        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def backtrack(i, path):
            if i >= len(s):
                outputs.append(path.copy())
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    path.append(s[i:j+1])
                    backtrack(j+1, path)
                    path.pop()
        backtrack(0, [])
        return outputs