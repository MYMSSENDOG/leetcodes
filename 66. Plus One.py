class Solution:
    def plusOne(self, digits):
        if not len(digits):
            return None
        num = 0
        for i in range(len(digits)):
            num *=10
            num+= digits[i]
        num+=1
        sn = str(num)
        digit = [0 for i in range(len(sn))]
        for i in range(len(sn)):
            digit[i] = sn[i]
        return digit

sol = Solution()
num = [1,2,3]
print(sol.plusOne(num))