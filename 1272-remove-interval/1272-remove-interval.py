class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        lst = []
        for interval in intervals:
            if interval[0] > toBeRemoved[1] or (interval[1] < toBeRemoved[0]):
                lst.append([interval[0], interval[1]])
            else:
                if interval[0] < toBeRemoved[0]:
                    lst.append([interval[0], toBeRemoved[0]])
                if interval[1] > toBeRemoved[1]:
                    lst.append([toBeRemoved[1], interval[1]])
        return lst
        