class Solution:
    def diffWaysToCompute(self, input: str) :
        """
        left parenthese가능한 위치
        1. 숫자앞
        right parenthese
        1. 숫자 뒤
        """
        def calc(expression)->int:

            if expression[1] == "+":
                return int(expression[0]) + int(expression[2])
            if expression[1] == "-":
                return int(expression[0]) - int(expression[2])
            if expression[1] == "*":
                return int(expression[0]) * int(expression[2])

        def dfs(expression, p):
            n = len(expression)
            i = p
            if n == 3:
                ret.append(calc(expression))
                return
            while i < n-2:
                dfs(expression[:i] + [str(calc(expression[i:i+3]))] + expression[i+3:],i)
                i+=2
            i = p
            if i -2>= 0 and i < n:
                dfs(expression[:i-2] + [str(calc(expression[i-2:i + 1]))] + expression[i + 1:], i - 2)
        ret = []
        stack = []
        if not input:
            return None
        if input.isnumeric():
            return [int(input)]
        i = 0
        while i < len(input):
            if input[i].isnumeric():
                start = i
                while i < len(input) and input[i].isnumeric():
                    i += 1
                stack.append(input[start:i])
            elif input[i] in "+-*":
                stack.append(input[i])
                i += 1
            else:
                i += 1
        dfs(stack, 0)
        return ret

sol = Solution()
expression = "2-1-1-1-1"

print(sol.diffWaysToCompute(expression))