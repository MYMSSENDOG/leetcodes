x = 551155

if x < 0:
    return False

s = x.__str__()
a = list(reversed(s))
ret = True
for i in range(((len(s)+1)/2))  :
    if a[i] == s[i]:
        continue
    else:
        return False
return True
