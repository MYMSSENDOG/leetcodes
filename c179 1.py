class Solution:
    def generateTheString(self, n: int) -> str:
        s = ""

        if not n:
            return ""
        if n % 2 == 0:
            s += "a"
            for _ in range(n-1):
                s += "b"
        else:
            for _ in range(n):
                s += "a"
        return s
n = 4
sol = Solution()
print(sol.generateTheString(n))