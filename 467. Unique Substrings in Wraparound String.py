
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        ret = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = 0
            cur_max = 0
            while i < len(p):
                if p[i] == c:
                        start = i
                        while i + 1 < len(p) and ord(p[i+1])%26 == (ord(p[i]) + 1)%26:
                            i+=1
                        end = i
                        cur_max = max(cur_max,end + 1 - start)
                        i = end+1
                else:
                    i+=1
            ret+=cur_max
        return ret







p = "abc"
sol = Solution()
print(sol.findSubstringInWraproundString(p))