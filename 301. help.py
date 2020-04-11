class Solution:
    def removeInvalidParentheses(self, s: str) :
        def helper2(s,left):
            if left == 0:
                return [s]
            ret = []
            dic = {}
            for i in range(len(s)):
                if s[i] == "(":
                    t = s[:i] + s[i+1:]
                    if t not in dic:
                        dic[t] = 1
                        ret += [s[:i] + k for k in helper2(s[i+1:], left-1)]
            return ret
        return helper2(s, 2)
sol = Solution()
s = "(()(()"
print(sol.removeInvalidParentheses(s))