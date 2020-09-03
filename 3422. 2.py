import collections
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.count = 0
        self.dp = {}
        self.dp[0] = collections.defaultdict(int)
        self.dp[0][0] = 1
        for i in range(len(characters)):
            self.dp[i+1] = collections.defaultdict(int)
            for j in range(i+2):
                self.dp[i+1][j] = self.dp[i][j] + self.dp[i][j - 1]
        #combination 계산 최적화
        pass
    def next(self) -> str:
        self.count += 1
        cur_count = self.count
        ret = ""
        idx = 0
        for i in range(self.length):
            dp = self.dp
            left_pos = len(self.characters) - idx - 1
            left_num = self.length - i - 1

            while cur_count > dp[left_pos][left_num]:
                cur_count -= dp[left_pos][left_num]
                left_pos -=1
                idx += 1
            ret += self.characters[idx]
            idx += 1
        return ret
    def hasNext(self) -> bool:
        if self.count == self.dp[len(self.characters )- 1][self.length - 1] +self.dp[len(self.characters )- 1][self.length]:
            return False
        return True

    def combi(self, a, b):
        ret = 1
        if b == 0:
            return 1
        for i in range(b):
            ret *= a
            a -= 1
        return ret

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
codes = ["CombinationIterator","next","hasNext","next","hasNext","next","hasNext"]
args = [["abc",2],[],[],[],[],[],[]]
codes = ["CombinationIterator","hasNext","next","hasNext","hasNext","next","next","hasNext","hasNext","hasNext","hasNext"]
args = [["chp",1],[],[],[],[],[],[],[],[],[],[]]
com = CombinationIterator(args[0][0], args[0][1])
for i, e in enumerate(codes, 1):
    if e == "next":
        print(com.next())
    else:
        print(com.hasNext())