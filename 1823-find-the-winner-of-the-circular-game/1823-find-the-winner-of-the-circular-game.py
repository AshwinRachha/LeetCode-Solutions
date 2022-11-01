class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = deque([i for i in range(1, n + 1)])
        #print(queue)
        count = 1
        while len(queue)!=1:
            while count != k:
                node = queue.popleft()
                queue.append(node)
                count += 1
            node = queue.popleft()
            count = 1
        return queue[0]
            