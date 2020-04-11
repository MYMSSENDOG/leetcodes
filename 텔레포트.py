
input_line = input().split()

N = int(input_line[0])#도시수
W = int(input_line[1])#H
H = int(input_line[2])#W

loc = []
for i in range(N):
    loc.append([int(x) for x in input().split()])
def getDistance(a, b):
    x = min (abs(a[0] - b[0]), H + a[0] - b[0], b[0]-a[0] + H)
    y = min (abs(a[1] - b[1]), W + a[1] - b[1], b[1]-a[1] + W)
    return x + y
def merge_sort(array, value):
    if len(array) == 0:
        array.append(value)
    else:
        l = 0
        r = len(array) - 1
        m = 0
        while l < r:
            m = (r + l)//2
            if array[m][0] > value[0]:
                r = m
            elif array[m][0] < value[0]:
                l = m + 1
            elif array[m][0] == value[0]:
                array.insert(m, value)
                break
        if array[l][0] < value[0]:
            array.insert(l+1, value)
        else:
            array.insert(l-1,value)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.parent = self
def isSameParent(n1, n2):
    while n1.val != n1.parent.val:
        n1 = n1.parent
    while n2.val != n2.parent.val:
        n2 = n2.parent
    if n1.val == n2.val:
        return True
    else:
        return False
def merge(n1,n2):
    while n2.val != n2.parent.val:
        n2 = n2.parent
    n2.parent = n1

tree = [TreeNode(x) for x in range(N)]


sorted_dist = []
for i in range(1,N):
    for j in range(i):
        #dist[i][j] = getDistance(loc[i], loc[j])
        #merge_sort(sorted_dist, [getDistance(loc[i], loc[j]),i,j])
        sorted_dist.append([getDistance(loc[i], loc[j]),i,j])
        #dist [j][i] = dist[i][j]
sorted_dist.sort()
ret = 0
line = 0
index = 0
while line<N-1:
    t = sorted_dist[index]
    distance = t[0]
    n1 = tree[t[1]]
    n2 = tree[t[2]]
    if isSameParent(n1,n2):
         index +=1
         continue
    else:
        merge(n1,n2)
        print(n1.val, n2.val)
        line+=1
        ret += distance
        index +=1
print(ret)
