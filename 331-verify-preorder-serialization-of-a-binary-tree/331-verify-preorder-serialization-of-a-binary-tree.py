class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        stack = []
        preorder = preorder.split(',')
        for c in preorder:
            stack.append(c)
            while len(stack) > 2 and stack[-3] != '#' and stack[-2] == '#' and stack[-1] =='#':
                stack.pop(); stack.pop(); stack.pop();
                stack.append('#')
            print(stack)
        return len(stack) == 1 and stack[0] == '#'
        