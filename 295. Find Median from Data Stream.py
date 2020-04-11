class MedianFinder:

    def __init__(self):
        self.q = []

        self.med_idx = -1
    def addNum(self, num: int) -> None:
        if not self.q:
            self.q.append(num)
        else:
            q = self.q
            l = 0
            r = len(q)
            while l < r:
                m = (r + l)//2
                if q[m] == num:
                    q.insert(m, num)
                    return
                elif q[m] > num:
                    r = m
                else:
                    l = m+1
            q.insert(l, num)
    def findMedian(self) -> float:
        n = len(self.q)
        if n % 2 == 1:
            return self.q[n//2]
        else:
            return (self.q[n // 2] + self.q[n // 2 - 1])/2

a = MedianFinder()

func = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
args =[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
for i, f in enumerate(func[1:],1):
    if f == "addNum":
        a.addNum(args[i][0])
        print("addNum", args[i][0])
    else:
        print(a.findMedian())
