class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = 0
        if len(a)<= len(b):
            a, b = b,a
        a = a[::-1]
        b = b[::-1]
        ret = ""
        for i in range(len(b)):
            t = int(b[i]) + int(a[i]) + add
            if t == 0:
                ret += "0"
                add = 0
            elif t == 1:
                ret +="1"
                add = 0
            elif t == 2:
                ret += "0"
                add = 1
            elif t == 3:
                ret += "1"
                add = 1
        for i in range(len(b),len(a)):
            t = add + int(a[i])
            if t == 1:
                ret += "1"
                add = 0
            elif t == 2:
                ret += "0"
                add = 1
            elif t == 0:
                ret += "0"
                add = 0
        if add == 1:
            ret += "1"
        ret = ret[::-1]
        return ret
sol = Solution()
a = "1010"
b = "1"
print(sol.addBinary(a,b))