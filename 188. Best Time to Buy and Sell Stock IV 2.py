class Solution:
    def maxProfit(self, k: int, prices):
        if len(prices) <=1 or k == 0:
            return 0
        ASCENDING = False
        row = []
        peak = []

        for i in range(1,len(prices)):
            #작아지다 커지면
            if prices[i] > prices[i-1] and not ASCENDING:
                row.append(prices[i-1])
                ASCENDING = True
                #커지다 작아지면
            elif prices[i] < prices[i-1] and ASCENDING  and row:
                peak.append(prices[i-1])
                ASCENDING = False
        if prices[-1] >= prices[-2] and row:
            peak.append(prices[-1])
        n = len(row)

        if k >= n:
            return sum(peak) - sum(row)
        row.append(0)
        dp = [[0]*(k+1) for i in range(n + 1)]
        for i in range(1,k+1):
            local_max = -row[0]
            for j in range(1, n + 1):
                dp[j][i] = max(dp[j - 1][i], peak[j-1] + local_max)
                local_max = max(local_max, dp[j][i-1] - row[j])
        return dp[-1][-1]

        """
        dp[i][j] 는 peak[i]를 포함하며 j개의 transaction
        dp[i][j] = x 라 할 때 dp [i+1][j] = 
        max(dp[i][j],   max(for k in range(0,i):)  
                            dp[k][j-1]  - row[k + 1]
                            dp[k][j-1] - row[k + 1]의 최대값은 현재값과 다음 dp[k+1][j-1] + row[k+2]
                        + peak[i+1]
        dp[i][0] = 0 for all i
        
                            
        """

prices = [3,3]
k = 2
sol = Solution()
print(sol.maxProfit(k,prices))
#point that can be selling day
