distance = 0
que = deque([(0,0)])
offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
(-1, -2), (-2, -1), (-2, 1), (-1, 2)]
visited = set()
while que:
for _ in range(len(que)):
curr_x, curr_y = que.popleft()
if (curr_x, curr_y) == (x, y):
return distance
for off_x, off_y in offsets:
next_x, next_y = curr_x + off_x, curr_y + off_y
if (next_x, next_y) not in visited:
visited.add((next_x, next_y))
que.append((next_x, next_y ))
distance += 1