class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = ""
        while n:
            r = (n-1)%26 + 1
            ret = chr(64+r) + ret
            n  = (n-1)//26
        return ret
sol = Solution()
n = 1
print(sol.convertToTitle(n))