class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        need_pop = False
        q = []
        while i < len(s):
            c = s[i]
            if c.isnumeric():
                start = i
                while i<len(s) and s[i].isnumeric():
                    i +=1
                cur_num = int(s[start:i])
                if not need_pop:
                    q.append(cur_num)
                else:
                    op = q.pop(-1)
                    t = q.pop(-1)
                    if op == "*":
                        q.append(t * cur_num)
                    elif op == "/":
                        q.append( t // cur_num)
                    need_pop = False
            elif c in "+-*/":
                q.append(c)
                if c in "*/":
                    need_pop = True
                i+=1
            elif c == " ":
                i += 1
                continue
        i = 1
        ret = q[0]
        while i < len(q):
            if q[i] == "+":
                ret += q[i+1]
            elif q[i] == "-":
                ret -= q[i + 1]
            i+=2
        return ret
sol = Solution()
s = "3+5/2/2 + 1 + 5 * 3 + 626 / 66"
print(sol.calculate(s))