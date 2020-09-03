
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.change_counter = self.makeCounter()
        self.count = 0


    def next(self) -> str:
        self.count = 1
        cur_str = self.characters
        ret = ""
        for i in range(len(self.change_counter)):
            idx = self.change_counter[i][0]
            ret += cur_str[idx]
            cur_str = cur_str[:idx] +cur_str[idx+1:]
            self.change_counter[i][1] += 1
            if self.change_counter[i][1] == self.change_counter[i][2]:
                self.change_counter[i][1] = 0
                self.change_counter[i][0] = (self.change_counter[i][0] + 1) % (len(self.characters) - i)
        return ret



    def hasNext(self) -> bool:
        if self.count == 1:
            if self.change_counter[0][0] == 0 and self.change_counter[0][1] == 0:
                return False
        return True

    def permutation(self, a, b):
        ret = 1
        if b == 0:
            return 1
        for i in range(b):
            ret *= a
            a -= 1
        return ret
    def makeCounter(self):
        a = len(self.characters) - 1
        b = self.length - 1
        ret = []
        while b >= 0:
            ret.append([0,0,self.permutation(a, b)])# 현재 몇번째 해야되냐, 바꿀때까지 카운트 , 최대카운트
            a -= 1
            b -= 1
        return ret
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
codes = ["CombinationIterator","next","hasNext","next","hasNext","next","hasNext"]
args = [["abc",2],[],[],[],[],[],[]]
com = CombinationIterator(args[0][0], args[0][1])
for i, e in enumerate(codes, 1):
    if e == "next":
        print(com.next())
    else:
        print(com.hasNext())