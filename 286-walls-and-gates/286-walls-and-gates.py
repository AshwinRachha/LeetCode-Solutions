class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))
        distances = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            r, c, level = queue.popleft()
            for d in distances:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >=rows or nc >= cols or rooms[nr][nc] != 2147483647:
                    continue
                rooms[nr][nc] = min(rooms[nr][nc], level + 1)
                queue.append((nr,nc, level + 1))
                
                
            