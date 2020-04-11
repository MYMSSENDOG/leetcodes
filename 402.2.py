class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        while k:
            z = num.find("0")
            if z != -1 and z + 1 < k:
                k -= z
                num = num[z:]
                num = num.lstrip("0")
            else:
                for i in range(len(num) - 1):
                    if num[i] > num[i + 1]:
                        num = (num[:i] + num[i+1:]).lstrip("0")
                        break
                else:
                    num = num[:-1]
                k-=1
        if not num:
            return "0"
        return num



sol = Solution()
num = "1020304050"
k = 3
print(sol.removeKdigits(num,k))