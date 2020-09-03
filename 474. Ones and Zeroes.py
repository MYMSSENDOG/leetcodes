class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        strs.sort(key = lambda x: x.count("1"))
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for str in strs:
            o = str.count("1")
            z = str.count("0")
            for y in range(m,-1,-1):
                for x in range(n,-1,-1):
                    if y - z >= 0 and x - o >= 0:
                        dp[y][x] = max(dp[y - z][x-o] + 1,dp[y][x])
                    if x - o< 0 :
                        break
        return dp[-1][-1]




sol = Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(sol.findMaxForm(strs,m,n))
