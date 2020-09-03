class Solution:
    def maxScore(self, s: str) -> int:
        l = 0
        r = s.count("1")
        ret = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                l+=1
            else:
                r -=1
            ret = max(ret, l+r)
        return ret