class Solution:
    def decodeString(self, s: str) -> str:
        
        numStack = []
        stringStack = []
        number = ""
        string = ""
        for ch in s:
            if ch.isdigit():
                number += ch
            elif ch == "[":
                numStack.append(int(number))
                stringStack.append(string)
                number = ""
                string = ""
            elif ch == "]":
                string = stringStack.pop() + string * numStack.pop()  
            else:
                string += ch
        return string