class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        ret = ""
        for i in range(n):

            if i > 0 and s[i-1] == s[-1]:
                prefix = s[:i]
                sufix = s[n - i:n]
                if prefix == sufix:
                    ret = prefix
        return ret
sol = Solution()
s = "ababab"
print(sol.longestPrefix(s))