class Solution:
    def minCut(self, s: str) -> int:
        #1 이 전의 솔루션을 구해서 가장 조각이 적은 것의 경우를 구함
        #2 완전 다르게 함
        #3 dp솔루션이 생각은 났으나 시간이 부족해서 다음에 하자
        def is_palindrome(s1):
            m = len(s1)
            for i in range(m//2):
                if s1[i] != s1[~i]:
                    return False
            return True
        m = len(s)
        ispal = [[False]*(x+1) for x in range(m)]
        dp = [x for x in range(m)] + [-1]
        for i in range(m):
            for j in range(i,-1,-1):
                if s[i] == s[j] and( i-j<2 or ispal[i-1][j+1] == True):
                    ispal[i][j] = True
                    dp[i] = min(dp[i], dp[j-1]+1)
        return dp[-2]
sol = Solution()
s = "aab"
print(sol.minCut(s))