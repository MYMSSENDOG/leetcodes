class Solution:
    def entityParser(self, text: str) -> str:
        d = {}
        d["&quot;"] = '\"'
        d["&apos;"] = "'"
        d["&amp;"] = "&"
        d["&gt;"] = ">"
        d["&lt;"] = "<"
        d["&frasl;"] = "/"
        ret = ""
        i = 0
        while i < len(text):
            c = text[i]
            if c == "&":
                start = i
                j = i + 1
                temp = "&"
                while j < len(text) and j != ";":
                    if text[j] == "&":
                        temp = "&"
                    elif text[j] == ";":
                        temp += text[j]
                        if temp in d:
                            ret+= d[temp]
                        else:
                            ret+= temp
                        break
                    else:
                        temp+=text[j]
                    j+=1
                i = j+1
            else:
                ret+= c
                i+=1
        return ret



text = "leetcode.com&frasl;problemset&frasl;all"
sol = Solution()
print(sol.entityParser(text))