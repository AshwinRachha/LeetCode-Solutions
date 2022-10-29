class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        s = list(s)
        
        for c in s:
            
            if not stack:
                stack.append([c, 1])
            else:
                if c == stack[-1][0]:
                    if stack[-1][1] == k-1:
                        stack.pop()
                    else:
                        stack[-1][1] += 1
                else:
                    stack.append([c, 1])
        return "".join([c*count for c, count in stack])
        