import collections
dict = collections.defaultdict(int)
f = open("word.txt","r")
while True:
    line = f.readline()
    if not line:
        break
    words = line.split()
    for w in words:
        dict[w] +=1
f.close()
q = []
for i in dict:
    q.append([dict[i], i])
q.sort()
for i in reversed(q):
    print(i[1], i[0])