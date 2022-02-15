class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return - 1
        
        graph = defaultdict(list)
        for v1, v2 in connections:
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = set()
        def dfs(node):
            visited.add(node)    
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(node)
                    dfs(nei)
        count = 0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count - 1