class MyHashSet:

    def __init__(self):
        self.max_size = 500000
        self.count = 0
        self.hash1 = [500000]* self.max_size
        self.hash2 = [500000]* self.max_size
    def add(self, key: int) -> None:
        idx = self.hash_function(key)
        if self.hash1[idx] == self.max_size or self.hash1[idx] == key:
            self.hash1[idx] = key
        else:
            self.hash2[idx] = key

    def remove(self, key: int) -> None:
        idx = self.hash_function(key)
        if self.hash1[idx] == key:
            self.hash1[idx] = self.max_size
        elif self.hash2[idx] == key:
            self.hash2[idx] = self.max_size
    def contains(self, key: int) -> bool:
        idx = self.hash_function(key)
        if self.hash1[idx] == key:
            return True
        elif self.hash2[idx] == key:
            return True
        return False
    def hash_function(self, key: int):
        t = key % self.max_size
        idx = (9*t + 7*t**2 + 11*t**3 + 17*t**4 + 23*t**5 + 29*t**6 + 31*t**7 + 123*t%3 + 778*t%7 + 679*t%11 + t%11121 )%self.max_size
        return idx
        """
        Returns true if this set contains the specified element
        """

codes = ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
args = [[],[1],[2],[1],[3],[2],[2],[2],[2]]
hash = MyHashSet()
for c, e in zip(codes[1:],args[1:]):
    i = e[0]
    if c == "add":
        print(hash.add(i))
    elif c == "contains":
        print(hash.contains(i))
    elif c == "remove":
        print(hash.remove(i))
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)