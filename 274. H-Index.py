class Solution:
    def hIndex(self, citations) -> int:
        """
        O(n) solution
        n = len(citations)
        bucket = [0] * (n+ 1)

        for i in citations:
            if i >= n:
                bucket[n] +=1
            else:
                bucket[i] +=1
        count = 0
        for i in range(n,-1,-1):
            count += bucket[i]
            if count>=i:
                return i
        """

        ret = 0
        citations.sort()

        for i in reversed(citations):
            if i > ret:
                ret+=1
        return ret


sol = Solution()
citations = [1,2,3,4]
print(sol.hIndex(citations))