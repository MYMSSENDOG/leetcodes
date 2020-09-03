class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"
        idx = 2
        pos = 2
        strs = ["1", "2"]
        ret = 1
        while pos <n-1:
            add = strs[int(s[pos])-2] # int(s[pos])-2 =
            s += add * int(s[idx])
            pos +=int(s[idx])
            ret -= (int(s[pos])-2) * int(s[idx])

            idx +=1
        if len(s) > n and s[n] == "1":
            ret-=1
        return ret


n=  7
sol = Solution()
print(sol.magicalString(n))