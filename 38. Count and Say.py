class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1:
            return None
        if n == 1 :
            return "1"
        ret = "1"
        temp = ""
        count = 0
        for i in range(n - 1):
            cur = ret[0]
            count = 0
            for c in ret:
                if c == cur:
                    count += 1
                else :
                    temp += str(count)
                    temp += cur
                    cur = c
                    count = 1
            ret = temp
            temp  = ""
            ret += str(count)
            ret += cur
        return ret

sol = Solution()
print(sol.countAndSay(6))