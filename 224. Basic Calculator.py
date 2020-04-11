class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = None
        operator = None
        operand = None

        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            if c == "(":
                stack.append([cur, operator])
                cur = None
                pass
            elif c == ")":
                last = stack.pop()
                if last[1] == "+":
                    cur = last[0] + cur
                elif last[1] == "-":
                    cur = last[0] - cur
                elif last[0] == None and last[1] == None:
                    cur = cur
                    operator = None
            elif c == " ":
                pass
            elif c == "+":
                operator = "+"
            elif c == "-":
                operator = "-"
            elif c.isnumeric():
                start = i
                while i<n and s[i].isnumeric():
                    i+=1
                if cur==None:
                    cur = int(s[start:i])
                else:
                    operand = int(s[start:i])
                    if operator == "+":
                        cur = cur + operand
                    else:
                        cur = cur - operand
                    operator = None
                    operand = None

                i-=1
            i+=1
        return cur




sol = Solution()
s = "0-1"
print(sol.calculate(s))