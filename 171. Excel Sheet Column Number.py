class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            ret *= 26
            d = ord(s[i])- ord("A") + 1
            ret += d
        return ret
sol = Solution()
s = "CA"
print(sol.titleToNumber(s))