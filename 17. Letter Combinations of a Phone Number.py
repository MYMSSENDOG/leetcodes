from string import ascii_lowercase
a = dict()

st = 0
num = 3
for i in range(2,10):
    if i == 7 or i == 9:
        num = 4
    else:
        num = 3
    a[str(i)] = ascii_lowercase[st:st+num]
    st = st+ num

digits = "2355"
n = 1
for i  in digits:
    n *= len(a[i])

ret = [""] * n
interval = n
for i in digits:
    div = len(a[i])
    interval = interval/div
    for j in range(len(ret)):

        ret[j] += a[i][int((j/interval)%div)]
print(ret)