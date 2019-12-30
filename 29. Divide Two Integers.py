class Solution:# */% 사용 안됨
    def divide(self, dividend: int, divisor: int) -> int:
        ret = 0
        pow = 1
        MINUS = False
        divisor_list = []
        temp = divisor


        if dividend < 0:
            dividend = -dividend
            MINUS = not MINUS
        if divisor < 0:
            divisor = -divisor
            MINUS = not MINUS

        while temp <= dividend:
            divisor_list.append([temp,pow])
            temp += temp
            pow += pow

        j = len(divisor_list) - 1
        while(divisor<=dividend and dividend >= 0):
            temp = divisor_list[j][0]
            temp_pow = divisor_list[j][1]
            if dividend - temp >= 0:
                ret += temp_pow
                dividend -= temp
            j -= 1
        if MINUS == True:
            ret = -ret
        if ret < -2**31:
            ret = -2**31
        elif ret > 2**31 - 1:
            ret = 2**31 - 1

        return ret

sol = Solution()
print(sol.divide(-7,3))