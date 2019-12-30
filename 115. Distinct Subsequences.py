class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #딕셔너리로 풀어보자
        dic = dict()
        for i in range(len(t)):
            dic[t[i]] = []
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]].append(i)
        """
        def helper(s_i, t_i):
            if len(s) - s_i< len(t) - t_i:
                return 0
            ret = 0
            if t_i == len(t) - 1:
                for i in range(s_i,len(s)):
                    if s[i] == t[t_i]:
                        ret += 1
                return ret
            for i in range(s_i,len(s)):
                if s[i] == t[t_i]:
                    ret += helper(i + 1,t_i+1)
            return ret

        return 
        """
        def helper(t_i, s_i):
            if t_i == len(t):
                return 1
            if not dic[t[t_i]] or len(s) - s_i <len(t) - t_i:
                return 0
            ret = 0
            for i in dic[t[t_i]]:
                if i >= s_i:
                    ret += helper(t_i + 1, i + 1)
            return ret
        return helper(0,0)



sol = Solution()

S = "abcabc"
T = "abc"
print(sol.numDistinct(S,T))