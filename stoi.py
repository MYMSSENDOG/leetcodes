
def myAtoi(str):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    int_max = 2147483647
    minus = False

    str = str.replace(' ', "")
    if len(str)  == 0:
        return 0
    if str[0] == '-':
        minus = True
        str = str[1:]
    elif str[0] == '+':
        minus = False
       str = str[1:]
    ret = 0
    if len(str) == 0:
        return 0
    elif str[0] == "0":
        return 0
    for c in str:
        if c not in numbers:
            break
        else:
            ret = ret * 10 + int(c)

        if minus == False and ret > int_max:
            return int_max
        elif minus == True and ret > int_max + 1:
            return -int_max - 1
    if minus == True:
        ret = -ret
    return ret

myAtoi("  -42")