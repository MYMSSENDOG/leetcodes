import math
input_line = input().split()

p1 = int(input_line[0])
p2 = int(input_line[1])
p3 = int(input_line[2])
k = int(input_line[3])
ret = []

#1 1~x까지 하나 하나  이 숫자가 3개로 소인수분해되는지

dict = {}
h1,h2,h3 = math.log10(p1),math.log10(p2),math.log10(p3)
for a in range(41):
    for i in range(a-1):
        for j in range(i+1,a):
            ret.append(i* h1 + (j-i-1)*h2+ (a-1-j)*h3)
            dict[i* h1 + (j-i-1)*h2+ (a-1-j)*h3] = [i, j-i-1, a-1-j]

ret.sort()
t = dict[ret[k-1]]
print(p1 ** t[0] * p2 ** t[1] * p3 ** t[2])