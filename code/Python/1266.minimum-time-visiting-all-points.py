class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            nowPoint = points[i]
            nextPoint = points[i+1]
            time += max(abs(nowPoint[0]-nextPoint[0]),
                        abs(nowPoint[1]-nextPoint[1]))
        return time
