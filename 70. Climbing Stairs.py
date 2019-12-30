class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        s1 = 1
        s2 = 2
        for i in range(3,n+1):
            temp = s1+s2
            s1 = s2
            s2 = temp
        return temp

sol = Solution()
n = 5
print(sol.climbStairs(n))