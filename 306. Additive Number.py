class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(p1, p2, i):

            for k in range(i ,len(num)):
                if k > i and num[i] == "0":
                    break
                if int(num[i:k+1]) == p1 + p2:
                    if k == len(num)-1:
                        return True
                    t = dfs(p2, int(num[i:k+1]), k+1)
                    if t:
                        return t
            return False

        n = len(num)
        for i in range(0,n//2):
            if i > 0 and num[0] == "0":
                continue
            for j in range(i+1,n):
                if j > i+1 and num[i+1] == "0":
                    break
                p1 = int(num[:i+1])
                p2 = int(num[i+1:j+1])
                if dfs(p1, p2, j+1):
                    return True
        return False


num = "0123"
sol = Solution()
print(sol.isAdditiveNumber(num))