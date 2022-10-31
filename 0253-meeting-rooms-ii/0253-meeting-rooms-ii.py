class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        intervals.sort()
        heap = []
        for start, end in intervals:
            if not heap or heap[0] > start:
                heapq.heappush(heap,end)
            else:
                heapq.heappushpop(heap, end)
        return len(heap)
        """
        used_rooms = 0
        n = len(intervals)
        start_timings = sorted(interval[0] for interval in intervals)
        end_timings = sorted(interval[1] for interval in intervals)
        start, end = 0, 0
        while start < n:
            if start_timings[start] >= end_timings[end]:
                used_rooms -= 1
                end += 1
            used_rooms += 1
            start += 1
        return used_rooms
            