class Solution:
    def numSquares(self, n: int) -> int:

        #mathematical solution
        def is_square(n):
            return n ** (1/2) == int(n ** (1/2))

        if is_square(n):
            return 1
        while n %4 == 0:
            n = n//4
        for i in range(1, int(n**(1/2))+1):
            if is_square(n - i*i):
                return 2
        if n & 7 == 7:
            return 4
        return 3


        """
        #bfs
        ret = {}
        squares = []
        for i in range(1,n+1):
            if i*i<=n:
                ret[i*i] = 1
            else:
                break

        for i in range(1, n + 1):
            if i * i <= n:
                squares.append(i*i)
            else:
                break

        q = [i for i in ret]
        total = 1
        if n in q:
            return 1
        while q:
            total +=1
            for i in range(len(q)):
                t = q.pop(0)

                for j in squares:
                    t2 = t + j
                    if t2< n and t2 not in ret:
                        ret[t2] = total
                        q.append(t2)
                    elif t2 == n:
                        return total
                    elif t2> n:
                        break
                    elif t2 in ret:
                        continue
        return ret[n]
        """

        """
        #static dp solution time limit
        dp = [0]
        while len(dp)<=n:
            m = len(dp)
            cntSquare = 9999999
            i = 1
            while i**2<=m:
                cntSquare = min(cntSquare, dp[m-i*i] + 1)
                i+=1
            dp.append(cntSquare)
        return dp[-1]
        """

        """
        dp solution time limit
        
        dp = [999999999] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i], 1 + dp[i-j**2])
                j+=1
        return dp[-1]
        
        
        
        """

        """
        memoization dfs solution solved!
        
        memo = [0] * (n+1)
        def dfs(n):
            if  memo[n] != 0 :
                return memo[n]
            if n **(1/2) == int(n **(1/2)):
                memo[n] = 1
                return 1
            m = 9999
            i = int(n**(1/2))
            while i>0:
                m =  min (m, dfs(n-i**2)+1)
                if m == 2:
                    break
                i-=1
            memo[n] = m
            return memo[n]
        return dfs(n)
        
        
        """

sol = Solution()
n =111111

print(sol.numSquares(n))