class Solution:
    def numberToWords(self, num: int) -> str:
        Eng1 = ["","One", "Two", "Three", "Four","Five","Six","Seven","Eight","Nine"]
        Eng10 = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        Eng20=["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        def name(s_num):
            ret = ""
            while len(s_num):
                c = s_num[0]
                if len(s_num) == 3 and c != "0":
                    ret+= Eng1[int(c)] + " " + "Hundred "
                elif len(s_num) == 2:
                    if int(c) >=2:
                        ret += Eng20[int(c)] +" "
                    elif c == "1":
                        one = int(s_num[1])
                        ret += Eng10[one]
                        break
                elif len(s_num) == 1:
                    ret += Eng1[int(c)]
                s_num = s_num[1:]
            return ret.rstrip()

        num = str(num)
        ret = ""
        if num == "0":
            return "Zero"

        if len(num) > 9:
            ret += name(num[0:len(num) - 9]) + " Billion "
            num = num[len(num) - 9: ]
            num = num.lstrip("0")
        if len(num) >6:
            ret += name(num[0:len(num) - 6]) + " Million "
            num = num[len(num) - 6:]
            num = num.lstrip("0")
        if len(num)>3:
            ret += name(num[0:len(num) - 3]) + " Thousand "
            num = num[len(num) - 3:]
            num = num.lstrip("0")
        ret += name(num)
        return ret.strip()


sol = Solution()
num = 1010101
print(sol.numberToWords(num))