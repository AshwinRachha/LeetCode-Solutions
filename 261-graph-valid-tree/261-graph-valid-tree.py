class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            else:
                visit.add(node)
                for nei in graph[node]:
                    if nei == parent:
                        continue
                    if not dfs(nei, node):
                        return False
                return True
        return dfs(0, -1) and len(visit) == n