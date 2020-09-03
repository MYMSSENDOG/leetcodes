# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input().split(";")
start_point = int(user_input[0])
memory_space = [int(i) for i in user_input[1].split()]

ret = "0; "
count = 0
cur = start_point
while 1:
    data_type = memory_space[cur]
    if data_type == 1:
        ret += "1 " + str(memory_space[cur+1]) + " "
        count += 1
        break
    else:
        ret += "0 " + str((count + 1)*2) + " "
        count += 1
        cur = memory_space[cur+1]
while count <4:
    ret += "0 0 "
    count +=1
print(ret.rstrip())
