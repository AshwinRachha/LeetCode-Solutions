class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific, atlantic = set(), set()
        Q = deque()
        rows, cols = len(heights), len(heights[0])
        
        def dfs(r, c, elevation, visit):
            # Out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            # Water cannot flow from lower elevation to a higher elevation
            if elevation > heights[r][c]:
                return
            # If already Visited
            if (r, c) in visit:
                return
            visit.add((r,c))
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            dfs(r - 1,c, heights[r][c], visit)
            
        # For the co-ordinates aligned with pacific, put them in Pacific Set
        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows-1, c, heights[rows-1][c], atlantic)
        # For the co-ordinates aligned with the atlantic, put them in the Atlantic Set
        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols-1], atlantic)
        
        # Get the intersection of both sets which should be the answer.
        return list(pacific.intersection(atlantic))