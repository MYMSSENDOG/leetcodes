class Solution:
    def addOperators(self, num: str, target: int):

        ret= []
        def dfs(exp, left_num, val, last):
            if not left_num:
                if val == target:
                    ret.append(exp)
                return
            for i in range(0, len(left_num)):
                t = left_num[:i+1]
                if i == 0 or  (i>0 and t[0] != "0"):
                    dfs(exp +"+"+ t, left_num[i+1:], val + int(t), int(t))
                    dfs(exp +"-"+ t, left_num[i + 1:], val-int(t), -int(t))
                    dfs(exp +"*"+ t, left_num[i + 1:], val - last + last * int(t), last * int(t))
        for i in range(0,len(num)):
            t = num[:i+1]
            if i == 0 or (i > 0 and t[0] != "0"):
                dfs(t,num[i+1:],int(t),int(t))
        return ret



sol = Solution()
num = "105"
target = 5
print (sol.addOperators(num,target))
