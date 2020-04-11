class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        l = len(s)
        def helper(length, num): # if length == 4 and num == 5 it is to 4999
            if length == 1:
                if num>=1:
                    return 1
                else:
                    return 0
            if num == 0:
                return 0
            if num == 1:
                return (length-1) * 10 ** (length-2)
            total = 0

            a = helper(length, 1)
            total += a
            for i in range(num-1):
                total += a
                if i == 0:
                    total += 10 ** (length-1)
            return total
        cur = ""
        total = 0
        for i, c in enumerate(s):
            if i != len(s) - 1:
                total +=  helper(l, int(c))
                total += cur.count("1") * int(c) * 10 ** (l-1)
                l -=1
                cur += c
            else:
                total += cur.count("1") * (int(c) + 1)
                if int(c) != 0:
                    total+=1
        return total



sol = Solution()
n =1111
print(sol.countDigitOne(n))