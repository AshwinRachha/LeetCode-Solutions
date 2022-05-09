class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        n = len(digits)
        output = []
        
        def backtrack(index, temp):
            if index >= n:
                output.append("".join(temp))
                return
            else:
                for char in dic[digits[index]]:
                    temp.append(char)
                    backtrack(index + 1, temp)
                    temp.pop()
        
        backtrack(0, [])
        return output