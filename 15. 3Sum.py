nums = [3,0,-2,-1,1,2]
sol = set()

minus = []
plus = []
a = dict()
zero = 0
for n in nums:
    if n in a:
        a[n] = a[n] + 1
    else:
        a[n] = 1
    if n>0:
        plus.append(n)
    elif n<0:
        minus.append(n)
    else:
        zero += 1

for i1, n1 in enumerate(minus):
    for i2, n2 in enumerate(plus):
        s = n1 + n2
        if s + n1 == 0:
            if a[n1] < 2:
                continue
        elif s + n2 == 0:
            if a[n2] < 2:
                continue
        if -s in a:
            el = [n1, n2, -(n1 + n2)]
            el.sort()
            sol.add(tuple(el))
        else:
            continue
        """
        #if there's no hash
        if s<0:
            if -s in plus[i2+1:]:
                el = [n1, n2, -(n1 + n2)]
                el.sort()
                sol.add(tuple(el))

        elif s >0:
            if -s in minus[i1 + 1:]:
                el = [n1, n2, -(n1 + n2)]
                el.sort()
                sol.add(tuple(el))
        """

if zero >= 3:
    sol.add((0, 0, 0))


#sol = list(set(map(tuple, sol)))
print(sol)
#2개의 합을 해쉬 등록