class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split('/')
        stack = []
        for token in path:
            if token == '.' or token == '':
                continue
            if token == '..' and stack:
                stack.pop()
                continue
            if token == '..' and not stack:
                continue
            else:
                stack.append(token)
        
        return '/' + '/'.join(stack)