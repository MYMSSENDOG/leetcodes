class Solution:
    def maxProfit(self, k: int, prices):
        if len(prices) <=1 or k == 0:
            return 0
        ASCENDING = False
        ret = 0
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
        if prices[-1] > prices[-2]:
            peak.append(prices[-1])
        n = len(row)
        max_dif = [[0]*(n+1) for i in range(n+1)]
        for i in range(n):
            r = row[i]
            for j in range(i,n):
                p = peak[j]
                max_dif[i][j] = max(p-r, max_dif[i][j-1])
        if k >= n:
            return sum(peak) - sum(row)

        def helper(array, k, sum):
            pass
        #너무 비효율적인것 같다.
        #사실 코딩어케할지 떠오르지도않음..

        return max_dif



prices = [1,5,2,6,3,8,9]
k = 2
sol = Solution()
print(sol.maxProfit(k,prices))
#point that can be selling day
"""
1 previous price is lower than now
2 next price is lower than now or today is last

# point that might sell stack
1 pre is higher than now or first day
2 next is higher than now




n rows and n peaks
need to pick k highest low-peak difference
the possible number of case is nCk and getting max_difference execute with in O(n)time complexity
so the whole time complexity is O( nCk * n)
"""