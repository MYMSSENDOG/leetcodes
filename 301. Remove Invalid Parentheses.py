class Solution:
    def removeInvalidParentheses(self, s: str) :
        ret = []
        s = s.rstrip("(")
        s = s.lstrip(")")

        def helper(s, last_i, last_j, paren):
            l = 0
            r = 0
            for i, p in enumerate(s[last_i:],last_i):
                if p == paren[0]:
                     l+=1
                elif p == paren[1]:
                    r +=1
                if l - r>= 0:
                    continue
                for j in range(last_j,i+1):
                    if s[j] == paren[1] and (j == 0 or (j >0 and s[j-1] != paren[1] )):
                        helper(s[:j] + s[j+1:],i,j,paren)
                return
            s = s[::-1]

            if paren[0] == "(":
                print(s[::-1])
                helper(s, 0, 0, [")","("])
            else:
                ret.append(s)
        helper(s,0,0, ["(", ")"])
        return ret
    """
    이게 되는 이유
    left to right 에서
    parethesis는 vaild + xxxx
     or xxxx가 될것이다. 
     valid 의 경우 valid의 생김새가 전부 다르므로 xxx가 어떻게 validate되어도 상관 없이 다르며
     xxxx만 있을 경우 right to left 로 한번에 validate되기 때문에 모두 서로 다르다.
    """


sol = Solution()
s = "())())"
print(sol.removeInvalidParentheses(s))