class Solution:
    def getRow(self, rowIndex: int) :
        ret = [1] * (rowIndex+1)
        def comb(x,n):
            m = 1
            d = 1
            for i in range(n):
                m *= x
                x -= 1
                d *= n
                n -= 1
            return int(m/d)

        for j in range(1, (rowIndex) // 2 + 1):
            ret[j] = comb(rowIndex, j)
        for j in range((rowIndex) // 2 + 1, rowIndex+1):
            ret[j] = ret[~j]
        return ret
sol = Solution()
k = 3
print(sol.getRow(k))