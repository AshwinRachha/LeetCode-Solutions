class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # Stack of tuples -> (letter, count of occurence)
        stack = []
        n, i = len(s), 0
        while i < n:
            if not stack or s[i] != stack[-1][-1]:
                stack.append(s[i])
            else:
                stack[-1] += s[i]
                if len(stack[-1]) == k:
                    stack.pop()
            i+=1
            
        return "".join(stack)
        