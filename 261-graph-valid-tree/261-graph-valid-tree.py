class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False
            else:
                seen.add(node)
                for child in graph[node]:
                    if child == parent:
                        continue
                    if not dfs(child, node):
                        return False
                return True
            
        return dfs(0, -1) and len(seen) == n

        