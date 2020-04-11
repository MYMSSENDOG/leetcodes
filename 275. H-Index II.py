class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        if not citations:
            return 0
        ret = 0
        for i in reversed(range(n)):
            if citations[i] > ret and citations[i] != 0:
                ret +=1
            else:
                return ret
        return ret


sol = Solution()
citations = [1]
print(sol.hIndex(citations))