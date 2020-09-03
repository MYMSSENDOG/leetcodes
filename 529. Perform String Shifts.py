class Solution:
    def stringShift(self, s: str, shift) -> str:
        r = 0
        for i in shift:
            d,c = i
            r +=c if d == 1 else -c
        r %= len(s)
        s = s[-r:] + s[:-r]
        return s


sol = Solution()
s = "abcdefg"
shift =  [[1,1],[1,1],[0,2],[1,3]]
print(sol.stringShift(s,shift))