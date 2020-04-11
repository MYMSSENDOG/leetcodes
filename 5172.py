import collections

class Solution:
    def largestMultipleOfThree(self, digits) ->  str:
        s = sum(digits)
        d = collections.defaultdict(int)
        ret = ""
        n1, n2 = 0,0
        if s == 0:
            if 0 in digits:
                return "0"
            return ""
        if s%3 == 0:
            digits.sort(reverse=True)
            for i in digits:
                ret+= str(i)
            return ret

        for i in digits:
            if i != 0 and i%3 !=0:
                if i%3 == 1:
                    n1 +=1
                else:
                    n2 +=1
                d[i] +=1

        if s%3 == 1:
            if not n1 and not n2>1:
                if 0 in digits:
                    return "0"
                return ""
        if s%3 == 2:
            if not n2 and not n1>1:
                if 0 in digits:
                    return "0"
                return ""
        to_del = []
        if s %3 == 1:
            if n1:
                for i in [1, 4, 7]:
                    if i in d:
                        to_del.append(i)
                        break
            else:
                for i in [2,5,8]:
                    for j in range(d[i]):
                        to_del.append(i)
                        if len(to_del) == 2:
                            break
        if s %3 == 2:
            if n1:
                for i in [2, 5, 8]:
                    if i in d:
                        to_del.append(i)
                        break
            else:
                for i in [1,4,7]:
                    for j in range(d[i]):
                        to_del.append(i)
                        if len(to_del) == 2:
                            break
        digits.sort(reverse=True)
        for i in digits:
            if i in to_del:
                to_del.remove(i)
            else:
                ret+= str(i)
        return ret














sol =Solution()
digits = [5,8]
print(sol.largestMultipleOfThree(digits))