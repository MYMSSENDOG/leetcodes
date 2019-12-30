class Solution:
    def maxPoints(self, points) -> int:
        def gcd(n1, n2):
            n = max(n1,n2)
            d = min(n1,n2)
            if d == 0:
                return 1
            while n % d != 0:
                r = n % d
                n = d
                d = r
            return d
        if not points or not points[0]:
            return 0
        dict = {}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                if x1 == x2:
                    key = ("i", x1)
                    dict[key] =0

                else:
                    g = gcd(x1-x2,y2-y1 )
                    minus = 1
                    if y2 - y1 >0:
                        minus = -1
                    key = ((y2-y1)//g*minus, (x1-x2)//g*minus , -(y2-y1)//g*minus * x1 - (x1-x2)//g*minus * y1)
                    dict[key] = 0
        for i in range(len(points)):
            for j in dict:
                #수직선일경우
                if j[0] == "i":
                    if j[1] == points[i][0]:
                        dict[j] +=1
                else:
                    a = j[0]
                    b = j[1]
                    c = j[2]
                    if a * (points[i][0]) + b * (points[i][1]) + c == 0:
                        dict[j] +=1
        M = 1
        for i in dict:
            M = max(M, dict[i])
        return M
        """
                if x1 == x2:
                    key = ("i", x1)
                    if key in dict:
                        if [x2, y2] not in dict[key]:
                            dict[key] += [[x2,y2]]
                    else:
                        dict[key] = [[x1,y1],[x2,y2]]
                else:
                    a_d_b = (y2-y1)/(x1-x2)
                    key = (a_d_b, -a_d_b*x1-y1 )
                    if key in dict:
                        if [x2, y2] not in dict[key]:
                            dict[key] += [[x2, y2]]
                    else:
                        dict[key] = [[x1, y1], [x2, y2]]

        M = 1
        for i in dict:
             M = max(len(dict[i]),M)
        return M
        """

sol = Solution()
points = [[0,0],[94911151,94911150],[94911152,94911151]]
print(sol.maxPoints(points))
