class Solution:
    def printVertically(self, s: str):
        ss = s.split(" ")
        m = 0
        for word in ss:
            m = max(m, len(word))
        ret = ["" for _ in range(m)]
        for word in ss:
            for i, c in enumerate(word):
                ret[i]+=c
            if len(word)<m:
                for j in range(i+1, m):
                    ret[j] += " "
        for i in range(len(ret)):
            ret[i] = ret[i].rstrip(" ")
        return ret
sol = Solution()
s = "CONTEST IS COMING"
print(sol.printVertically(s))