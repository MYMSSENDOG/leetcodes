

class PeekingIterator:
    def __init__(self, iterator):
        self.q = iterator[0]
        self.q_size = len(iterator)
        self.index = 0
    def peek(self):
        return self.q[self.index]

    def next(self):
        self.index += 1
        return self.q[self.index - 1]



    def hasNext(self):
        if self.index  < self.q_size:
            return True
        return False



command = ["PeekingIterator","next","peek","next","next","hasNext"]
args = [[[1,2,3]],[],[],[],[],[]]
iter = PeekingIterator(args[0])
for i,e  in enumerate(command[1:],1):
    if e == "next":
        print(iter.next())
    elif e == "peek":
        print(iter.peek())
    elif e == "hasNext":
        print(iter.hasNext())