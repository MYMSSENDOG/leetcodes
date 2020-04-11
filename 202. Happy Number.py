class Solution:
    def isHappy(self, n: int) -> bool:

        dict = {}


        while 1:
            q = []
            while n:
                q.append(n % 10)
                n = n // 10
            s = 0
            for i in q:
                s += i**2
            if s == 1:
                return True
            if s in dict:
                return False
            dict[s] = 1
            n = s



n = 19
sol = Solution()
print(sol.isHappy(n))