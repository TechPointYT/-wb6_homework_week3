class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        lastE = float("-inf")
        arrow = 0        
        for bal in points:
            if bal[0] <= lastE:
                lastE = min(lastE, bal[1])
            else:
                arrow += 1
                lastE = bal[1]
        return arrow
