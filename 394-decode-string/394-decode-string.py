class Solution:
    def decodeString(self, string: str) -> str:

        nums = []
        strs = []
        num = ""
        s = ""
        for i, ch in enumerate(string):
            if ch.isdigit():
                num += ch
            elif ch == "[":
                nums.append(int(num))
                strs.append(s)
                num = ""
                s = ""
            elif ch == "]":
                s =  strs.pop() + nums.pop() * s
            else:
                s += ch

        return s