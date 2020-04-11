class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        cur = ""
        prev = ""
        i = 0
        num = 1
        while i<len(s):
            c = s[i]
            if c.isnumeric():
                start = i
                while s[i].isnumeric():
                    i+=1
                num = int(s[start:i])
                i-=1
            elif c == "[":
                stack.append(num)
                num = 1
            elif c == "]":
                cur = prev + cur * stack.pop(-1)
            else:
                cur += c
            i+=1
        return cur

sol = Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s))