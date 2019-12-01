class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
#       We'll be iterating over every two points to find diagonal distance and if not either vertical or horizontal
        for i in range(len(points) - 1):
            time += max([abs(points[i][0]-points[i+1][0]),abs(points[i][1] - points[i+1][1])])
        return time