class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = ""
        t = path.split("/")
        p = []
        for i in t:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len(p):
                    p.pop()
                else:
                    pass
            else:
                p.append(i)
        for i in p:
            ret += "/" + i
        if ret == "":
            ret += "/"
        return ret
sol = Solution()
path  = "/a//b////c/d//././/.."
print(sol.simplifyPath(path))