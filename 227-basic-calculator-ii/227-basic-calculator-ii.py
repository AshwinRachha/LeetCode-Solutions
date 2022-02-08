class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = ''.join(s.split())
        n = len(s); i = 0
        sign = 1
        while i < n:
            if s[i].isnumeric():
                num = ''
                while i < n and s[i].isnumeric():
                    num += s[i]
                    i+=1
                stack.append(sign * int(num))
                sign = 1
            else:
                if s[i] in '*/':
                    operation = s[i]; i+=1
                    num1 = stack.pop(); num2 = ''
                    while i < n and s[i].isnumeric():
                        num2 += s[i]
                        i+=1
                    if operation == '*':
                        stack.append(num1 * int(num2))
                        sign = 1
                    else:
                        stack.append(int(num1 / int(num2)))
                        sign = 1
                else:
                    if s[i] == '-':
                        sign = -1
                    i+=1
        print(stack)
        return sum(stack)
                    