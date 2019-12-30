
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for i in range (m+n):#s[:i]까지 맞냐
            x = min(i+1,m)
            y = i+1 - x

            while x >=0 and y<=n :
                if x == 0:
                    dp[x][y] = dp[x][y - 1 ] and s3[i] == s2[y - 1]
                elif y == 0:
                    dp[x][y] = dp[x-1][y] and s3[i] == s1[x-1]
                else:
                    dp[x][y] |= (dp[x - 1][y] and s3[i] == s1[x - 1]) or (dp[x][y - 1] and s3[i] == s2[y-1])
                x -= 1
                y +=1
        return dp[m][n]



sol = Solution()
s1 = "1"
s2 = ""
s3 = "1"
print(sol.isInterleave(s1,s2,s3))
