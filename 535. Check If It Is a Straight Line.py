class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates) < 2:
            return False
        # ax + b = y
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x1 == x2:
            axis = x1
            for x, y in coordinates[2:]:
                if x != axis:
                    return False
        else:
            a = (y2 - y1) / (x2 - x1)
            b = y1 - a * x1
            for x, y in coordinates[2:]:
                if a* x + b != y:
                    return False
        return True



sol = Solution()
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(sol.checkStraightLine(coordinates))