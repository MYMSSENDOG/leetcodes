class Solution:
    def generate(self, numRows: int):
        ret = []
        for i in range(1, numRows+1):
            ret.append([1]*i)
            for j in range(1,(i-1)//2 + 1):
                ret[i-1][j] = ret[i-2][j-1] + ret[i-2][j]
            for j in range((i - 1) // 2 + 1,i):
                ret[i - 1][j] = ret[i-1][~j]
        return ret
sol = Solution()
n = 5
print(sol.generate(5))