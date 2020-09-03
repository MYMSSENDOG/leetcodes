import bisect
import heapq
repeat = int(input())
for _ in range(repeat):
    N = int(input())
    A = [int(a) for a in input().split(" ")]
    ret = ""
    prev = 0
    h = []
    for i in range(len(A)):
        heapq.heappush(h,A[i])
        if h[0] >= prev+1:
            prev +=1
        else:
            heapq.heappop(h)
        ret+= " " + str(prev)
    print("Case #" + str(_ + 1) + ":" + ret)