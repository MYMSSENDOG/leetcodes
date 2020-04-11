class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False

        def gcd(a, b):
            s = max(a,b)
            t = min(a,b)
            if t == 0:
                return s
            while s%t !=0:
                s, t = t, s%t
            return t
        g =  gcd(gcd(x,y),z)
        if gcd(x,y) == g:
            return True

        return False
sol = Solution()
x,y,z = 0,0,0
print(sol.canMeasureWater(x,y,z))