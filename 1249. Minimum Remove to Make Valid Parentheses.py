class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ret = ""
        stack = 0
        dict = {0:[]}

        for i, e in enumerate(s):
            ret += e
            if e == "(":
                stack +=1
                dict[0].append(len(ret) - 1)
            elif e == ")":
                stack -=1
            else:
                pass
            if stack == 0:
                dict[0] = []

            if stack <0:
                ret = ret[:-1]
                stack +=1
        if stack >0:
            t = stack
            for i in reversed(dict[0]):
                # i = index of (
                ret = ret[:i] + ret[i+1:]
                t -=1
                if t == 0:
                    break

        return ret
s = "))(("
sol = Solution()
print(sol.minRemoveToMakeValid(s))