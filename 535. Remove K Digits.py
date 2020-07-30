import heapq
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        idx = 0
        for n in num:
            while stack and stack[-1] >n and k:
                stack.pop()
                k -= 1
            if k == 0:
                break

            stack.append(n)

            idx +=1
        ret = ""
        for _ in  range(k):
            stack.pop()
        for c in stack:
            ret += c
        if (ret + num[idx:]).lstrip("0"):
            return (ret + num[idx:]).lstrip("0")
        else:
            return "0"



sol = Solution()
num = "125"
k = 1
print(sol.removeKdigits(num, k ))
#1110099
#110099
#111009