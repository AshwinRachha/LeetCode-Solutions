class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        check, stack = None, []
        for num in preorder:
            while stack and num > stack[-1]:
                check = stack.pop()
            if check!=None and check > num:
                return False
            stack.append(num)
        return True