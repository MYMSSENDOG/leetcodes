class Solution:
    def minWindow(self, s: str, t: str) -> str:
#t가 전부 들어가는 가장 작은 배열 인듯..
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""

        dic = dict()
        dic2 = dict()


        left = 0
        ret = ""
        for i in t:
            dic[i] = dic[i] + 1 if i in dic else 1
        for i in range(len(s)):
            if s[i] in dic:
                left = i
                dic2[s[i]] = 1
                break
        right = left

        while len(s) - left + 1 >= len(t) and right<len(s):
            exeed = True
            for k in dic:
                if k not in dic2:
                    exeed = False
                    break
                elif dic[k] > dic2[k]:
                    exeed = False
                    break

            if exeed:
                if ret != "":
                    ret = s[left:right+1] if len(ret)> right - left + 1 else ret
                else:
                    ret = s[left:right+1]
                not_match = True
                for l in range(left+1,len(s)):
                    if s[l] in dic:
                        dic2[s[left]] -= 1
                        left = l
                        not_match = False
                        break
                if not_match:
                    return ret
            else:
                right +=1
                if right<len(s):
                    if s[right] in dic:
                        dic2[s[right]] = dic2[s[right]] +1 if s[right] in dic2 else 1
        return ret


sol = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(sol.minWindow(S,T))