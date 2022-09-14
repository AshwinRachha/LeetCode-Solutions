class Solution:
    def minInsertions(self, s: str) -> int:
        
        stack = []
        i, n = 0, len(s)
        ans = 0
        while i < n:
            if i < n and s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                if i < n - 1 and s[i:i+2] == '))':
                    if not stack:
                        ans += 1
                    else:
                        stack.pop()
                    i += 2
                elif i < n and s[i] == ')':
                    if stack:
                        ans += 1
                        stack.pop()
                    else:
                        ans += 2
                    i += 1
        return len(stack) * 2  + ans
