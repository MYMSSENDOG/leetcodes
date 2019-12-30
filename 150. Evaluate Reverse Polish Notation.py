class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operators = ["+","-","/","*"]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                operator = i
                n2 = stack.pop()
                n1 = stack.pop()
                if operator == "+":
                    stack.append(n1+n2)
                elif operator == "-":
                    stack.append(n1 - n2)
                elif operator == "*":
                    stack.append(n1 * n2)
                elif operator == "/":
                    minus = 1
                    if n1^ n2 <0:
                        minus = -1
                    val =minus * n1 // n2
                    stack.append(minus * val)
        return stack[0]
sol = Solution()
tok = ["4","-2","/","2","-3","-","-"]
print(sol.evalRPN(tok))