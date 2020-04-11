class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = [c for c in s]
        i = 0
        j = n - 1
        while i < j:
            while i < n and s[i] not in "aeiouAOUEI":
                i+=1
            while j >= 0 and s[j] not in "aeiouAOUEI":
                j-=1
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        ret = ""
        for i in range(n):
            ret += s[i]
        return ret
sol = Solution()
s = "leetcode"
print(sol.reverseVowels(s))