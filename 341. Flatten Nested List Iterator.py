# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation


class NestedIterator:

    def __init__(self, nestedList: NestedInteger):
        def helper(list):
            ret = []
            for i in list:
                if isInteger(i):
                    ret += [i]
                else:
                    ret += helper(i)
            return ret


        for i in nestedList:
            if isInteger(i):
                continue
            else:
                helper(i)
    def next(self) -> int:
        return self.nestedList.pop(0)
    def hasNext(self) -> bool:
        if self.nestedList:
            return True
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

n = NestedIterator()
nestedList = [[1,1],2,[1,1]]


