import collections
class Solution:
    def topKFrequent(self, nums, k: int) :
        #1. dictionary 활용 후 정렬 후 리턴
        d = collections. defaultdict(int)
        for i in nums:
            d[i] +=1
        i = 1
        heap = [None] * (len(d) + 1)
        for q, w in d.items():
            heap[i] = [q, w]
            cur = i
            while cur//2 >0:
                if heap[cur][1] > heap[cur//2][1]:
                    heap[cur], heap[cur//2] = heap[cur//2], heap[cur]
                    cur = cur//2
                else:
                    break
            i+=1
        ret = []
        n = len(heap)-1
        for _ in range(k):
            ret.append(heap[1][0])
            heap[1] = heap[n]
            cur = 1
            while cur*2<n:
                l = heap[cur*2][1]
                r = 0 if cur*2+1>n else heap[cur*2+1][1]
                if heap[cur][1] < max(l,r):
                    if l > r :
                        heap[cur], heap[cur*2] = heap[cur*2],heap[cur]
                        cur*=2
                    else:
                        heap[cur], heap[cur * 2+1] = heap[cur * 2+1], heap[cur]
                        cur = cur*2 + 1
                else:
                    break

            n-=1
        return ret

nums = [5,2,5,3,5,3,1,1,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums,k))