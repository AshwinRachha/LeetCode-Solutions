class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        graph = defaultdict(list)
        for i, (n1, n2) in enumerate(zip(leftChild, rightChild)):
            graph[i].append(n1)
            graph[i].append(n2)
            if root in graph[i]:
                root = i 
        visit = set()
        def dfs(node):
            if node == -1:
                return True
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            return True
        
        if not dfs(root) or len(visit)!=n:
            return False
    
        return True
            