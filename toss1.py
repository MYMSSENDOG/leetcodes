user_input = input()
ret = True
prev = None
for c in user_input:
    if prev == None:
        pass
    elif prev == "1":
        if c == "1":
            ret =  False
            break
    prev = c
if user_input[-1] == "1":
    ret = False
print(ret)