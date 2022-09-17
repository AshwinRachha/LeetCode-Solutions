class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            hrs, mins = time.split(":")
            minutes.append(int(hrs) * 60 + int(mins))
        minutes.sort()
        minutes.append(minutes[0] + 24 * 60)
        min_diff = 1440
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        return min_diff