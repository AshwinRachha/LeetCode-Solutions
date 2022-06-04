class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        
        min_moves = 0
        directions = [(2, 1), (1, 2), (2, -1), (-1, 2), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
        q = deque([])
        q.append((0, 0))
        seen = set()
        seen.add((0, 0))
        while q:
            size = len(q)
            for _ in range(size):
                x1, y1 = q.popleft()
                if x1 == x and y1 == y:
                    return min_moves
                for x2, y2 in directions:
                    new_x, new_y = x1 + x2, y1 + y2
                    if (new_x, new_y) not in seen:
                        q.append((new_x, new_y))
                        seen.add((new_x, new_y))
            min_moves += 1
            
            
            
        