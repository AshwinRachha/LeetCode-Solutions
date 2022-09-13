class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for comet in asteroids:
            if not stack or stack[-1] < 0 or (comet > 0 and stack[-1] > 0):
                stack.append(comet)
            else:
                while stack and stack[-1] > 0 and stack[-1] + comet <0:
                    stack.pop()
                if stack and stack[-1] +comet == 0:
                    stack.pop()
                elif not stack:
                    stack.append(comet)
                elif stack and stack[-1] < 0:
                    stack.append(comet)

        return stack
                