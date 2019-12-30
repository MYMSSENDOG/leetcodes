class Node:
    def __init__(self, k, v):
        self.val = v
        self.key = k
        self.pre = None
        self.next = None

class LRUCache:



    def __init__(self, capacity: int):
        self.capa = capacity
        self.keys = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.keys:
            t = self.keys[key]
            self._remove(t)
            self._add(t)
            return t.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            t = self.keys.pop(key)
            self._remove(t)
        n = Node(key,value)
        self.keys[key] = n
        self._add(n)
        if len(self.keys) > self.capa:
            removed_key = self.head.next.key
            self.keys.pop(removed_key)
            self._remove(self.head.next)

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        t = self.tail.prev
        t.next = node
        node.prev = t
        self.tail.prev = node
        node.next = self.tail



assemble = ["LRUCache","put","get","put","get","get"]
code = [[1],[2,1],[2],[3,2],[2],[3]]

a = LRUCache(code[0][0])
print(None)
for i,e  in enumerate(assemble[1:]):
    if e == "put":
        print(a.put(code[i + 1][0],code[i + 1][1]))
    elif e == "get":
        print(a.get(code[i + 1][0]))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
put put get put get put get get
1,1 2,2 1   3,3 2  4,4  1  3   
"""