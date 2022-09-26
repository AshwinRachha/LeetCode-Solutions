class Solution:
def equationsPossible(self, equations: List[str]) -> bool:
graph = defaultdict(list)
for equation in equations:
if equation[1] == "=":
a, b = ord(equation[0]) - ord('a'), ord(equation[-1]) - ord('a')
graph[a].append(b)
graph[b].append(a)
color = [-1] * 26
def dfs(node, c):
if color[node] == -1:
color[node] = c
for nei in graph[node]:
dfs(nei, c)
for i in range(26):
if color[i] == -1:
dfs(i, i)
for equation in equations:
if equation[1] == '!':
x = ord(equation[0]) - ord('a')
y = ord(equation[3]) - ord('a')
if color[x] == color[y]:
return False
return True