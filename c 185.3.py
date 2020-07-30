class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ret = 0
        cur = 0
        croak = "croak"
        q = [0,0,0,0,0]
        for c in croakOfFrogs:
            if c == "c":
                cur +=1
                q[4]+=1
                ret = max(ret, cur)
            else:
                for i in range(1, len(q)):
                    if q[i]!=0:
                        if croak[-i] == c:
                            q[i] -=1
                            q[i-1] +=1
                            if i == 1:
                                cur -=1
                            break
                else:
                    return -1
        if q[1] or q[2] or q[3] or q[4]:
            return -1
        return ret



sol = Solution()
croakOfFrogs = "croakcroakcroak"
print(sol.minNumberOfFrogs(croakOfFrogs))