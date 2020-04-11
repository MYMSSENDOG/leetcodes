class Solution:
    def fizzBuzz(self, n: int):
        ret = []
        for i in range(1, n+1):
            s = ""
            if i%3 == 0:
                s += "Fizz"
            if i %5 == 0:
                s += "Buzz"
            if not s:
                s += str(i)
            ret.append(s)
        return ret



sol = Solution()
n = 15
print(sol.fizzBuzz(n))