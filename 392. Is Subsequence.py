class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        j = 0
        for i in range(len(s)):
            j = t.find(s[i], j)
            if j == -1:
                return False
            j+=1
        return True



sol = Solution()
s = "abc"
t = "ab"
print(sol.isSubsequence(s,t))
