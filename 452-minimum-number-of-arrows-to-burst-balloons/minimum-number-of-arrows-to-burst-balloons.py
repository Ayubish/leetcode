class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        max_end = float("-inf")
        ans = len(points)
        for xs, xe in points:
            if xs <= max_end:
                ans -= 1
                max_end = min(max_end, xe)
            else:
                max_end = xe
        return ans

