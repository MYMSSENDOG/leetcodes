import collections
class StreamChecker:
    def __init__(self, words):
        self.root = {}
        self.letters = ""
        for word in words:
            cur = self.root
            for i in range(len(word))[::-1]:
                c = word[i]
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["end"] = 1

    def query(self, letter: str) -> bool:
        self.letters += letter
        cur = self.root
        for i in range(len(self.letters))[::-1]:
            c = self.letters[i]
            if c not in cur:
                return False
            cur = cur[c]
            if "end" in cur:
                return True
        return False

codes = ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query",
     "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query",
     "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query",
     "query", "query", "query", "query", "query"]
args = [[["abaa", "abaab", "aabbb", "bab", "ab"]], ["a"], ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["b"], ["b"], ["a"],
     ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["a"], ["a"],
     ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"]]
#codes = ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]
#args = [[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]
s = StreamChecker(args[0][0])

for i in range(1, len(args)):
    print(s.query(args[i][0]))