class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        first = intervals[0]
        for interval in intervals[1:]:
            if first[1] > interval[0]:
                return False
            first = interval
        return True