class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows, cols = len(maze), len(maze[0])
        def destination(r,c):
            if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and [r,c] != entrance:
                return True
            return False
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        steps = 0
        distances = [(1,0), (0,1),(-1,0),(0,-1)]
        while q:
            r, c, steps = q.popleft()
            if(destination(r, c)):
                return steps
            for x, y in distances:
                if r + x < 0 or r + x >= rows or c + y < 0 or c + y >= cols or maze[r+x][c+y] == '+':
                    continue
                maze[r+x][c+y] = '+'
                q.append((r+x, c+y, steps + 1))
        return -1
    
        