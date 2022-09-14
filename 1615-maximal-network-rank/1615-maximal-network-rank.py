class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for city1, city2 in roads:
            graph[city1].append(city2)
            graph[city2].append(city1)
        max_network = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                if i in graph[j] or j in graph[j]:
                    max_network = max(max_network, len(graph[i]) + len(graph[j])-1)
                else:
                    max_network = max(max_network, len(graph[i]) + len(graph[j]))
        return max_network