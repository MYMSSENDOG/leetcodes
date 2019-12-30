

n = 2
ret = []
def find(paren:str):
    left_left = n - paren.count('(')
    right_left = n - paren.count(')')
    if len(paren) == 2*n-2:
        if left_left == 1:
            paren += "()"
        elif left_left == 0:
            paren += "))"
        ret.append(paren)#return paren
        return
    if left_left == 0:
        for i in range(2*n - len(paren)):
            paren += ")"
        ret.append(paren)  # return paren
        return
    elif left_left - right_left < 0:
        find(paren + "(")
        find(paren + ")")
    elif left_left == right_left:
        find(paren + "(")

find("(")
print(ret)