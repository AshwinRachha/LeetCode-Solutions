class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(s, l, r):
            if l == 0 and r == 0:
                output.append(s)
            if l != 0:
                backtrack(s + "(", l - 1, r)
            if r > l:
                backtrack(s + ")", l, r - 1)
        backtrack("", n, n)
        return output
        