import heapq
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ret = []
        for c in num:
            if ret and c < ret[-1] and k:
                ret.pop()
                k -=1
            ret.append(c)
        return "".join(ret[:-k or None])


sol = Solution()
num = "125"
k = 0
print(sol.removeKdigits(num, k ))
#1110099
#110099
#111009