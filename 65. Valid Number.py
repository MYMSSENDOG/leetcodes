class Solution:
    def isNumber(self, s: str) -> bool:
            s = s.replace(" ","")
            if not len(s):
                return False
            sn = s.split("e")

            #e다음엔 정수
            if "e" in s:
                if len(sn)!=2:
                    return False
                try:
                    int(sn[1])
                    if "." not in sn[1]:
                        pass
                    else:
                        return False
                except:
                    return False

            try:
                float(sn[0])
            except:
                return False
            if sn[0][-1] ==" ":
                return False
            return True
sol = Solution()
v = ".1"
print(sol.isNumber(v))