class Solution:
    def groupAnagrams(self, strs):
        ret = []

        for s in strs:
            found = False
            dic = dict()
            for c in s:
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1
            for i in ret:
                if i[0] == dic:
                    i.append(s)
                    found = True
                    break
            if not found:
                ret.append([dic, s])
        for i in ret:
            del(i[0])
        return ret

sol = Solution()
strs= ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))