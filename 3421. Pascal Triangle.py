class Solution:
    def getRow(self, rowIndex: int):

        ret = [1] * (rowIndex + 1)
        mult = rowIndex
        div = 1

        for i in range(1, (rowIndex + 2) // 2):

            ret[i] = ret[i - 1] * mult // div
            mult -= 1
            div += 1
            ret[-i - 1] = ret[i]
        return ret
sol = Solution()
k = 3
print(sol.getRow(k))
