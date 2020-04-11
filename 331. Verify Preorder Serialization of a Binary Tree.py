class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        s = preorder.split(",")
        if preorder == "#":
            return True
        stack = [2] if s[0] != "#" else []
        for c in s[1:]:
            if not stack:
                return False
            if c != "#":
                for i in range(len(stack)):
                    stack[i]+=1
                stack+= [2]
            else:
                if not stack:
                    return False
                for i in reversed(range(len(stack))):
                    stack[i]-=1
                    if stack[i] == 0:
                        stack.pop(i)
        if not stack:
            return True
        return False


preorder = "1,3,5"
sol = Solution()
print(sol.isValidSerialization(preorder))