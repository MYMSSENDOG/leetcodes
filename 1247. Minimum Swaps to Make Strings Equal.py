class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x = s1.count("x") + s2.count("x")
        y = s1.count("y") + s2.count("y")
        if x %2 ==1 or y %2==1:
            return -1
        dif = 0
        x_dif = 0
        ret = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dif +=1
                if s1[i] == "x":
                    x_dif +=1
        y_dif = dif - x_dif
        ret += (x_dif//2)
        ret += (y_dif//2)
        if x_dif %2 == 1:
            ret += 2
        return ret

sol = Solution()
s1 = "xxyyxyxyxx"
s2 = "xyyxyxxxyx"
print(sol.minimumSwap(s1,s2))