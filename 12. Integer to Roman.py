num = [3,4,9,58,1994]
"""
I = 1 
V = 5 
X = 10
K  = 50
C  = 100
D = 500
M = 1000 

CM = 900
CD = 400
IV = 4
IX = 9
XL = 40
XC = 90

"""

roman = [["I","V"]
         ,["X","L"]
         ,["C","D"]
         ,["M"]]


for this_num in num:
    ret = ""
    i = 2
    thou = int(this_num/1000)
    for th in range(thou):
        ret += "M"
    #this_num = this_num%1000
    this_num -= thou * 1000
    while(i>=0):
        hund =int(this_num/(10**i))
        if hund == 4:
            ret += roman [i][0]
            ret += roman[i][1]
        elif hund == 9:
            ret += roman[i][0]
            ret += roman[i+1][0]
        else:
            if hund >= 5:
                ret += roman[i][1]
                hund -=5
            for c in range(hund):
                ret += roman[i][0]
        this_num = this_num%(10**i)
        i -= 1
    print(ret)