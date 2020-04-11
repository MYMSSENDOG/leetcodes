class Solution:
    def originalDigits(self, s: str) -> str:

        def helper(n, count):
            num_alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            alpha = num_alpha[n]
            for c in alpha:
                i = ord(c) - ord("a")
                a[i] -= count

        ret = [0] * 10
        a = [0] * 26
        single = ["z", "o" ,"w", "h" ,"u" ,"f", "x", "s", "g", "i"]
        for c in s:
            i = ord(c) - ord("a")
            a[i] +=1
        for i in range(0,10,2):
            ch = single[i]
            idx = ord(ch) - ord("a")
            ret[i] += a[idx]
            helper(i, a[idx])
        for i in range(1,10,2):
            ch = single[i]
            idx = ord(ch) - ord("a")
            ret[i] += a[idx]
            helper(i, a[idx])
        s= ""
        for i,e in enumerate(ret):
            s += str(i) * e
        return s
sol = Solution()
s = "fviefurofviefurofviefurofviefurofviefurofviefuroowoztneoerowoztneoerowoztneoerthree"
print(sol.originalDigits(s))