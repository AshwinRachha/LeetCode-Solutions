class Solution:
    
    def __init__(self):
        self.visited = set()
        self.queue = deque()
    
    def bfs(self, grid, rows, columns, r, c):
        
        self.queue = deque([[r, c]])
        while self.queue:
            r,c = self.queue.popleft()
            if (r, c) not in self.visited and grid[r][c] == '1':
                self.visited.add((r,c))
                
                if r != 0 and grid[r-1][c] == '1':
                    self.queue.append([r-1, c])
                if c!= 0 and grid[r][c-1] == '1':
                    self.queue.append([r, c-1])
                if r!=rows-1 and grid[r+1][c] == '1':
                    self.queue.append([r+1, c])
                if c!=columns - 1 and grid[r][c+1] == '1':
                    self.queue.append([r, c+1])
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, columns = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(columns):
                
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.bfs(grid, rows, columns, r, c)
                    count += 1
        return count