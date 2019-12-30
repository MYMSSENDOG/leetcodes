class Solution:
    def restoreIpAddresses(self, s: str):
        def is_valid(t):
            n = len(t)
            s= int(t)
            if n == 1:
                return True
            if n == 2:
                return True if s >= 10 and s <= 99 else False
            if n == 3:
                return True if s >= 100 and s <= 255 else False

        def assign(s, loc):
            n = len(s)
            ret = []
            if n>loc*3 or n<loc:
                return[]

            if loc == 1:
                if is_valid(s):
                    return [s]
                else:
                    return []

            for i in range(3):
                temp = s[:i+1]
                if is_valid(temp) and (loc-1<= n-i-1) and (loc-1)*3 >= n-i-1:
                    right = assign(s[i+1:],loc-1)
                    for p in right:
                        if len(p)!= 0:
                            ret += [temp + "." + p]

                else:
                    continue

            return ret

        return assign(s,4)

n = "222222"
sol = Solution()
print(sol.restoreIpAddresses(n))
