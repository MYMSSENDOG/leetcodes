class LinkedList:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class FirstUnique:
    def getAll(self):
        cur = self.head
        ret = []
        while cur:
            ret.append(cur.val)
            cur = cur.right
        print(ret)
    def __init__(self, nums):
        self.head = None
        self.tail = None
        self.d = {}
        for i in nums:
            self.add(i)


    def showFirstUnique(self) -> int:
        if not self.head:
            return -1
        else:
            return self.head.val
    def add(self, value: int) -> None:

        if value in self.d:
            t = self.d[value]
            if t:
                if t == self.tail:
                    self.tail = self.tail.left
                    #self.tail.right = None
                if t == self.head:
                    self.head = t.right
                if t.left:
                    t.left.right = t.right
                if t.right:
                    t.right.left = t.left
                self.d[value] = None
            else:
                return
        else:
            cur = LinkedList(value)
            self.d[value] = cur
            if not self.head:
                self.head = cur
                self.tail = cur
            else:
                self.tail.right = cur
                cur.left = self.tail
                self.tail = cur

codes = ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
args = [[[2,3,5]],[],[5],[],[2],[],[3],[]]


fu = FirstUnique(args[0][0])
fu.getAll()

for idx, c in enumerate(codes[1:], 1):
    if c == "showFirstUnique":
        print(fu.showFirstUnique())
    if c == "add":
        print(fu.add(args[idx][0]))
        fu.getAll()


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
