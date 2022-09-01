class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        merged = [intervals[0][1]]
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            earliest = min(merged)
            
            if start < earliest:
                merged.append(end)
            else:
                index = merged.index(earliest)
                merged[index] = end
        return len(merged)
    
   