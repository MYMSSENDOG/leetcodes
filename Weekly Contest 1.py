class Solution:
    def getNoZeroIntegers(self, n: int) :
        ret = []
        for i in range(1,n):
            n1 = i
            n2 = n-n1
            if not str(n1).count("0") and not str(n2).count("0"):
                return [int(n1),int(n2)]


sol = Solution()
n = 11
print(sol.getNoZeroIntegers(n))