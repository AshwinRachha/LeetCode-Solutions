class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculateDistance(point):
            x, y = point
            return (x**2 + y**2) ** (0.5)
        arr = []
        for point in points:
            arr.append((point, calculateDistance(point)))
        arr.sort(key = lambda x : x[1])
        return [l[0] for l in arr[:k]]