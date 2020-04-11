class Solution:
    def numSteps(self, s: str) -> int:
        c = int(s, 2)
        ret = 0
        while c!=1:
            if c%2 == 0:
                c//=2
            else:
                c+=1
            ret +=1
        return ret
s = "1101"
sol = Solution()
print(sol.numSteps(s))