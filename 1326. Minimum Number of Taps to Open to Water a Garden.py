class Solution:
    def minTaps(self, n: int, ranges) -> int:

        dp = [0] * (n+1)
        for i,e  in enumerate(ranges):
            if e == 0:
                continue
            start = max(0,i - e)
            end = min(n, i + e)
            dp[start] = max(dp[start], end - start+1)

        ret = 0
        i = 0
        while i < n+1:
            jump = dp[i]
            if i + jump > n:
                return ret + 1
            if jump == 0:
                return -1
            M = 0
            M_i = 0
            for j in range(i+1, i + jump): #
                if M < j + dp[j]-1:
                    M = j + dp[j]-1
                    M_i = j
            if M_i == 0:
                return -1
            i = M_i
            ret +=1
        return ret
sol = Solution()
ranges = [1,0, 4 ,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]
n = 35
print(sol.minTaps(n, ranges))