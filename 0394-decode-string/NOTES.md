class Solution:
def decodeString(self, s: str) -> str:
nums = []
strs = []
string = ""
num = ""
for i, ch in enumerate(s):
if ch.isdigit():
num += ch
elif ch == '[':
nums.append(int(num))
strs.append(string)
num = ""
string = ""
elif ch == ']':
string = strs.pop() * nums.pop() + string
else:
string += ch
return string