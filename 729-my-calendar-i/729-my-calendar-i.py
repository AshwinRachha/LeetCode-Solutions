from sortedcontainers import SortedList
import bisect

class MyCalendar:
    def __init__(self):        
        self.calendar = SortedList()
        
    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_right(self.calendar, (start, end))
        
        if (index > 0 and self.calendar[index-1][1] > start) or (index < len(self.calendar) and self.calendar[index][0] < end):
            return False
        self.calendar.add((start, end))
        return True
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)