class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        h = 0
        for c in s:
            if c == "(":
                l+-1
                h+=1
            elif c == ")":
                h-=1
                l = max(l-1, 0)
            elif c == "*":
                h+=1
                l = max(l-1, 0)
            if h < 0:
                return False
        return l == 0



#'(*()*))((*()*))()()()()(())**(()()()*)(())()((()))'

s = "((()))()(())(*()()())**(())()()()()((*()*))((*()*)"
sol = Solution()
print(sol.checkValidString(s))
