class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.strip().split()
        ret = ""
        for i in reversed(range(len(a))):
            ret += a[i] + " "
        ret.strip()
        return ret
sol = Solution()
s = "   hello    world!"
print(sol.reverseWords(s))