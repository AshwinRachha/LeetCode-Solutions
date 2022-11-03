class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        Create a matrix “rank” where rank[i][j] holds how highly friend ‘i' views ‘j’. This allows for O(1) comparisons between people
        
        1 2 3
        3 2 0
        3 1 0
        1 2 0
        
        """
        unhappy = 0
        pairMap = defaultdict(int)
        for p1, p2 in pairs:
            pairMap[p1] = p2
            pairMap[p2] = p1
        prefer = {}
        for i in range(n):
            for j in range(n-1):
                if i not in prefer:
                    prefer[i] = {}
                prefer[i][preferences[i][j]] = j
        for i in range(len(preferences)):
            for j in range(n-1):
                x = i
                y = pairMap[x]
                u = preferences[x][j]
                v = pairMap[u]
                if prefer[x][u] < prefer[x][y] and prefer[u][x] < prefer[u][v]:
                    unhappy+=1
                    break
        return unhappy
    
        