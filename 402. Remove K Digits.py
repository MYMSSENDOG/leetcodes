class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num) - num.count("0"):#n
            return "0"
        if not k:
            return num
        z = num.find("0")
        if  z != -1 and z + 1 <k:
            k -= z
            num = num[z:]
            num = num.lstrip("0")
            return self.removeKdigits(num, k)
        else:
            for i in range(len(num)-1):
                if num[i] > num[i+1]:
                    return self.removeKdigits(str(int(num[:i] + num[i+1:])), k-1)
                    break
            else:
                return self.removeKdigits(num[:-1], k - 1)

sol = Solution()
num = "1020304050"
k = 3
print(sol.removeKdigits(num,k))