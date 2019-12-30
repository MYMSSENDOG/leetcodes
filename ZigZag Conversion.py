
numRows = 7
s = "asd1as6dajgjgh61jg65h1j1s65d"

a = list(range(numRows))
a = a + list(range(numRows - 2, 0, - 1))
lists = []
for i in range(numRows):
    lists.append([])

k = 0
for ch in s:
    lists[a[k]].append(ch)
    k = (k + 1) % (numRows * 2 - 2)

ret = ""
for str in lists:
    for c in str:
        ret+=c



