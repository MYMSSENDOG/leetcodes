class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # convert
        dic = {"0":0, "1":1, "2":2, "3":3 , "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        dic2 = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
        if num1 == "0" or num2 == "0":
            return "0"
        int_num1 = 0
        int_num2 = 0
        t = 10**(len(num1)-1)
        for i in num1:
            int_num1+= t*dic[i]
            t //= 10
        t = 10**(len(num2)-1)
        for i in num2:
            int_num2 += t * dic[i]
            t //= 10
        int_ret = int_num1*int_num2
        ret = ""
        while int_ret>0:
            ret += dic2[int_ret%10]
            int_ret //= 10
        temp = ret[0]
        ret = ret[-1:0:-1]
        ret += temp
        return ret
sol = Solution()
num1 = "123126789"
num2 = "123124321"
print(sol.multiply(num1, num2))
print(str(int(num1)*int(num2)))