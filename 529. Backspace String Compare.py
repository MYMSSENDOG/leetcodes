class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1

        def find_next(STR, idx):
            if idx == -1:
                return "", -1
            cur =STR[idx]

            if  cur != "#":
                return cur, idx-1
            else:
                count = 0
                while idx >=0:
                    cur = STR[idx]
                    if cur == "#":
                        count +=1
                    else:
                        count -=1
                    if count <0:
                        return STR[idx], idx-1
                    idx-=1
                return "", -1


        while i !=-1  or j != -1:
            s, i = find_next(S,i)
            t,j = find_next(T,j)
            if s != t:
                return False
        return True

sol = Solution()
S = "ap"
T = "au#p"
print(sol.backspaceCompare(S,T))