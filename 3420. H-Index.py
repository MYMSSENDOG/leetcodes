import heapq
class Solution:
    def hIndex(self, citations) -> int:
        q = []
        h = 0
        for c in citations:
            if c > h:
                heapq.heappush(q, c)
            if len(q) > h:
                h += 1
                while q and q[0] < h+1:
                    heapq.heappop(q)
        return h


sol = Solution()
citations = [3,0,6,1,5]
print(sol.hIndex(citations))