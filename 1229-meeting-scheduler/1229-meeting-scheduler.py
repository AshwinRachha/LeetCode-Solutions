class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort()
        slots2.sort()
        a, b, m, n = 0, 0, len(slots1), len(slots2)
        
        while a < m and b < n:
            start1, end1 = slots1[a]
            start2, end2 = slots2[b]
            #print(start1, end1, start2, end2)
            start = max(start1, start2)
            end = min(end1, end2)
            if start + duration <= end:
                return [start , start + duration]
            else:
                if end2 < end1:
                    b += 1
                else:
                    a += 1
        return []
        