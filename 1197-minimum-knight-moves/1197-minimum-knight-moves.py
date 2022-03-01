class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        q = deque([(0,0)])
        seen = set()
        seen.add((0, 0))
        min_steps = 0
        nei = [(2, 1),(1,2), (-2, 1),(1, -2), (-1, 2),(2, -1), (-2, -1),(-1, -2)]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == (x, y):
                    return min_steps
                for x1, y1 in nei:
                    new_x, new_y = node[0] + x1, node[1] + y1
                    if (new_x, new_y) not in seen:
                        seen.add((new_x, new_y))
                        q.append((new_x, new_y))
            min_steps += 1
        return min_steps
            