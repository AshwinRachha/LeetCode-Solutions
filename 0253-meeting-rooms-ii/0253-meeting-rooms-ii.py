class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        heap = []
        for start, end in intervals:
            if not heap or heap[0] > start:
                heapq.heappush(heap,end)
            else:
                heapq.heappushpop(heap, end)
        return len(heap)
    