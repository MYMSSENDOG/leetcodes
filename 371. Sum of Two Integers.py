class Solution:
    def getSum(self, a: int, b: int) -> int:
        t = 0
        bit = 1
        ret = 0
        for _ in range(32):
            aa = 1 if a & bit else 0
            bb = 1 if b & bit else 0
            cur  = 0
            if t ^ aa ^ bb:
                cur = 1
                if t & aa & bb:
                    t = 1
                else:
                    t = 0
            else:
                cur = 0
                if t | aa | bb == 1:
                    t = 1
                else:
                    t = 0
            if cur:
                ret |= bit
            if _ == 30:
                bit *=-2
            else:
                bit *= 2


        return ret
sol = Solution()
a = -1
b = -1
print(sol.getSum(a,b))