import collections
class Tree:
    def __init__(self, letter = None):
        self.letter = letter
        self.child_trees = {}
    def enroll(self, letter):
        self.child_trees[letter] = Tree()

class StreamChecker:
    def __init__(self, words):
        self.q = []
        self.d = collections.defaultdict(list)
        self.root = Tree()
        for word in words:
            cur = self.root
            for i in range(len(word)):
                c = word[i]
                if c not in cur.child_trees:
                    cur.enroll(c)
                cur = cur.child_trees[c]
            cur.enroll("end")

    def query(self, letter: str) -> bool:

        cur_dir = self.d[letter]
        if  letter in self.root.child_trees:
            cur_dir.append(self.root.child_trees[letter])
        flag = False
        self.d = collections.defaultdict(list)
        for _ in range(len(cur_dir)):
            cur = cur_dir.pop(0)
            if "end" in cur.child_trees:
                flag = True
            for c in cur.child_trees:
                if c == "end":
                    continue
                self.d[c].append(cur.child_trees[c])
        return flag

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