class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(key = lambda a:a[1])
        ret = 1
        if not points or not points[0]:
            return 0
        prev_s, prev_e = points[0]

        for s, e in points[1:]:
            if s <= prev_e:
                continue
            else:
                ret+=1
                prev_e = e
        return ret        
sol = Solution()
points = [[1,2],[2,3],[3,4],[4,5]]
print(sol.findMinArrowShots(points))
