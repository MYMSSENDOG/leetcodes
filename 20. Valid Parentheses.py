
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        par = dict()
        par = {"(": 1, ")": 1, "[": 2, "]": 2, "{": 3, "}": 3}

        def push(p: str):
            stack.append(p)

        def pop() -> str:
            if len(stack) == 0:
                return ""
            return stack.pop()

        for c in s:
            if c == "(" or c == "{" or c == "[":
                push(c)
            elif c == ")" or c == "}" or c == "]":
                temp = pop()
                if temp == "":
                    return False
                if par[temp] == par[c]:
                    continue
                else:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True


s = "]"
so = Solution()
print(so.isValid(s))