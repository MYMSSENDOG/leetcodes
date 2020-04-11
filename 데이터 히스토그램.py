data=  input()
alphabet = [0] * 26
cur_mul = 1
mul_stack = []
cur_num = 0
prev = ""
for i in range(len(data)):

    if data[i].isalpha():
        additional = 1
        if prev.isnumeric():
            additional = cur_num
        idx = ord(data[i]) - ord("a")
        alphabet[idx] += cur_mul*additional
        cur_num = 0
    elif data[i].isnumeric():
        if cur_num!=0:
            cur_num *=10
            cur_num+=int(data[i])
        else:
            cur_num = int(data[i])
    elif data[i] == "(":
        if cur_num:
            mul_stack.append(cur_num)
            cur_mul *= cur_num
        else:
            mul_stack.append(1)
        cur_num = 0
    elif data[i] == ")":
        t = mul_stack.pop()
        cur_mul//=t
    prev = data[i]
for i in range(len(alphabet)):
    print(chr(ord("a")+i)+" " + str(alphabet[i]))

