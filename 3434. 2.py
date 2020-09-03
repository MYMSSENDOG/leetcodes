
class StreamChecker:
    def __init__(self, words):
        self.d = {}
        self.max_len = 0
        self.letters = ""
        self.ld = []
        for word in words:
            self.ld[len(word)] = 1
            self.max_len = max(self.max_len, len(word))
            self.d[word] = 1
    def query(self, letter: str) -> bool:
        self.letters += letter
        if len(self.letters) > self.max_len :
            self.letters = self.letters[1:]

        for i in self.ld:
            if self.letters[ - i:] in self.d:
                return True
        return False

codes = ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"]
args = [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]

s = StreamChecker(args[0][0])
for i in range(1, len(args)):
    print(s.query(args[i][0]))