# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
input1 = input().split()
input2 = input().split()
k_to_l = [int(i) for i in input1]
l_to_k = [int(i) for i in input2]

remain = 0
ret = ""
for i in range(len(k_to_l)):
    money = k_to_l[i] - l_to_k[i]
    if remain - money >= 0:
        ret += "0" + " "
        remain -= money
    else:
        ret += str(money - remain) + " "
        remain = 0
print(ret.rstrip())