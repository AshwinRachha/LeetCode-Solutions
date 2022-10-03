queue = deque([(root, 0)])
max_dist = 0
while queue:
size = len(queue)
_, level_head = queue[0]
for _ in range(size):
node, index = queue.popleft()
if node.left:
queue.append([node.left, 2*index])
if node.right:
queue.append([node.right, 2*index + 1])
max_dist = max(max_dist, index - level_head + 1)
return max_dist