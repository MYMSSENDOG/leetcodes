class Solution:
    def grayCode(self, n: int) :
        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        def recu(n:int, t: int):
            if n == 0:
                return
            if n == 1:
                return [t,t+1]

            else:
                ret = (recu(n-1,t+2**(n-1)))
                ret.reverse()
                return recu(n-1,t) + ret
        ret = (recu(n-1,2**(n-1)))
        ret.reverse()
        return recu(n-1,0)  + ret




n =3
sol = Solution()
print(sol.grayCode(n))