class Solution:
    def decodeString(self, s: str) -> str:

        def dfs(l, r):
            cur = ""
            num = 1
            i = l
            while i<r:
                c = s[i]
                if c.isnumeric():
                    start = i
                    while s[i].isnumeric():
                        i += 1
                    num = int(s[start:i])
                    i -= 1
                elif c == "[":
                    st = 1
                    start = i
                    i+=1
                    while st:
                        c = s[i]
                        if c == "[":
                            st +=1
                        elif c == "]":
                            st -=1
                        i+=1
                    end = i
                    cur += num * dfs(start+1, end-1)
                    continue
                else:
                    cur += c
                i+=1
            return cur
        return dfs(0,len(s))
sol = Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s))