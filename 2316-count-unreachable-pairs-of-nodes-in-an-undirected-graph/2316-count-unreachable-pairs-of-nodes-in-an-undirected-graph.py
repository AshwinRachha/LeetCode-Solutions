class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for v in edges:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            res = 1
            for n in graph[node]:
                res += dfs(n)
            return res
        
        components = []
        total_sum = 0
        
        for i in range(n):
            temp = dfs(i)
            if temp != 0:
                total_sum += temp
                components.append(temp)
        
        result = 0
        for i in components:
            result += (total_sum - i) * i
        return result//2
        
        
        
        
        