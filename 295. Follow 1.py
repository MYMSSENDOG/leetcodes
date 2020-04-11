"""
if 99% is in range of 0 ~ 100
keep -1 to - infinite as a variable and so on 101~
it's important just counting number of them
but at first ...
just maintain the q like first solution and if median is in 0~100(count the number and easily find it)


"""
class MedianFinder:
    def __init__(self):
        self.size = 0
        self.q = [0] * 101
    def addNum(self, num: int) -> None:
        self.q[num] +=1
        self.size +=1
    def findMedian(self) -> float:
        n = self.size
        total = 0
        m1 = -1
        m2 = -1
        for i in range(101):
            total += self.q[i]
            if total >= (n+1)//2:
                if m1 == -1:
                    m1 = i
            if total>= (n+1)//2 + 1:
                m2 = i
                break
        if n % 2 == 1:
            return m1
        return (m1 + m2) /2
a = MedianFinder()

func = ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
args =[[],[1],[2],[],[3],[]]
for i, f in enumerate(func[1:],1):
    if f == "addNum":
        a.addNum(args[i][0])
        print("addNum", args[i][0])
    else:
        print(a.findMedian())
