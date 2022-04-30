class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        
        for i, equation in enumerate(equations):
            graph[equation[0]][equation[1]]  = values[i]
            graph[equation[1]][equation[0]]  = 1 / values[i]
        
        def dfs(x, y, visited):
            
            if x not in graph or y not in graph: return -1
            if y in graph[x]:
                return graph[x][y]
            for key in graph[x]:
                if key not in visited:
                    visited.add(key)
                    temp = dfs(key, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[x][key]
            return -1
            
        ans = []
        for p, q in queries:
            ans.append(dfs(p, q, set()))
        return ans