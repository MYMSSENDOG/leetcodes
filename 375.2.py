class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp=[[0] * (n+2) for _ in range(n+3)]
        max_k = [[_] * (n+2) for _ in range(n+3)]

        for d in range(1,n):
            i = 1
            while i + d < n+1:
                j = i + d
                if j - i == 1:
                    dp[i][j] = i
                    i+=1
                    continue
                k = max_k[i][j-1]
                while k <=j and dp[i][k-1] <= dp[k+1][j]:
                    k+=1
                k-=1
                max_k[i][j] = k
                dp[i][j] = min(dp[k][j] + k-1, dp[k+1][j] + k, dp[i][k] + k + 1)
                i+=1
        return dp[1][n]


    """         k-=1
    
    작은쪽은 항상 버렸는데 작은쪽에 갈 경우 횟수가 더 클때, 그게 더 큰값이 되어버려서 오차 발생
    """
    """
    O(n^2 solution
    l r 이 있고 k 는 l_i 부터 r_i까지 움직인다.
    k = max(k |  f(l,x-1)<= f(x+1,r))
    즉
    f(ㅏ+1,r) + k 와
    f(l,k) + k+1을 비교하면 됨
    그리고 
    k(l, r) <= k (l+1,r)이므로 작은수부터 비교하면 됨
    """
sol = Solution()
n = 20
print(sol.getMoneyAmount(n))