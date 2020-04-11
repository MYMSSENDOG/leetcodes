class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == "6":
                s[i] = "9"
                break
        return int(s)
sol = Solution()
num = 99669
print(sol.maximum69Number(num))
