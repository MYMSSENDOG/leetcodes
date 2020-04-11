class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        ret = ""
        retu = ""
        hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        bit = 15
        d = 1
        for i in range(4):
            h = (num & bit)//d
            ret += hex[h]
            bit *= 16
            d *= 16
        for i in range(len(ret))[::-1]:
            retu+= ret[i]

        return retu.lstrip("0")
sol = Solution()
num = 255
print(sol.toHex(num))