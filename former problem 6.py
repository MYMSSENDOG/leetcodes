import random
class Solution:
    def create_lines(self, lines):
        a,b,d,f = lines
        e = a+b+-d
        c = a+f-d
        return [a,b,c,d,e,f]
    def getS(self, lines):
        a,b,c,d,e,f = lines
        h = (b + c) * (3 ** (1/2)) / 2
        return (a + d) / 2 * h + (b * c + e * f) / 4 * (3 ** (1/2))
    def getTriangles(self, lines):
        a,b,c,d,e,f = lines
        return (a*b + c*d + e*f + a*f + b*c + d*e) / 4 * (3 ** (1/2))
    def getSquares(self, lines):
        a, b, c, d, e, f = lines
        h1 = (b + c) * (3 ** (1 / 2)) / 2


    def main_(self):
        for i in range(1):
            a, b = [random.randint(1, 10),random.randint(1, 10)]
            d = random.randint(1, a+b - 1)
            f = random.randint(d-a + 1, d + 10)
            a,b,d,f = 2,2,2,2
            lines  = self.create_lines([a,b,d,f])
            real = self.getS(lines)
            fl = self.getTriangles(lines)
            print(real, fl, real  - fl)

sol = Solution()
sol.main_()

