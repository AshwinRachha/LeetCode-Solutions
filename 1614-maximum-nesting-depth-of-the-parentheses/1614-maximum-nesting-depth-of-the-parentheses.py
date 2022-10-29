class Solution:
    def maxDepth(self, s: str) -> int:
        
        """
        "" -> 0
        "(ashwin)" -> 0
        (A+B) -> max(A, B)
        """
        maximum = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
                maximum = max(maximum, len(stack))
            elif c == ")":
                    stack.pop()
        maximum = max(maximum, len(stack))
        return maximum
        