class Solution:
    
    def evaluate(self, expression, i):
        
        calc, operator = 0, '+'
        while expression[i] != ')':
            
            atom = expression[i]
            
            if atom == "+" or atom == "-":
                operator = atom
            else:
                if isinstance(atom, int):
                    num = atom
                else:
                    num, i = self.evaluate(expression, i+1)
                    
                if operator == "+":
                    calc += num
                else:
                    calc -= num
            
            i += 1
            
        return calc, i
    
    def calculate(self, s: str) -> int:
        
        digits = {str(i) for i in range(10)}
        expression = ['(']
        for c in s:
            if c == ' ':
                continue
            elif c not in digits:
                expression.append(c)
            elif isinstance(expression[-1], int):
                expression[-1] = expression[-1] * 10 + int(c)
            else:
                expression.append(int(c))
        
        expression.append(')')
        result , _ = self.evaluate(expression, 1)
        return result
        