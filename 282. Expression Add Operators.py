class Solution:
    def addOperators(self, num: str, target: int):
        ret = []
        if not num:
            return []
        if len(num) == 1:
            if int(num) == target:
                return [num]

        # n is expression before pos
        # pos is to insert operator


        operators = ["+", "-", "*", ""]

        def dfs(n, pos):
            #if pos < len(n) and n[pos] != "0" and n[pos-1] != "0":
            if len(n) == pos:
                if calc(n) == target:
                    ret.append(n)
                return
            for i in range(pos, len(n)):
                for op in operators:
                    if op == "":
                        end = i-1
                        while end >= 0 and n[end].isnumeric():
                            end-=1
                        if n[end+1] == "0":
                            return

                    t = n[:i] + op + n[i:]
                    dfs(t, i+2)
        dfs(num, 1)

        return ret





sol = Solution()
num = "123456789"
target = 45
print (sol.addOperators(num,target))
