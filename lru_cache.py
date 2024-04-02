class Node:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.key}, {self.val}"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = dict()
        self.first = None
        self.last = None

    def __repr__(self):
        return f"{self.LRU}, 1 -> {self.first}, -1 -> {self.last}"

    def update(self, node: Node) -> None:
        if not self.first:
            self.first = self.last = node
            self.capacity -= 1
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
            if node.key in self.LRU:
                if self.first.key == node.key:
                    self.first = self.first.next
                    self.first.prev = None
                else:
                    elem = self.LRU[node.key]
                    elem.prev.next = elem.next
                    elem.next.prev = elem.prev
            else:
                if self.capacity:
                    self.capacity -= 1
                else:
                    del self.LRU[self.first.key]
                    self.first = self.first.next
                    self.first.prev = None
        self.LRU[node.key] = node

    def get(self, key: int) -> int:
        if key in self.LRU:
            new_elem = Node(key, self.LRU[key].val)
            self.update(new_elem)
            return self.LRU[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        new_elem = Node(key, value)
        self.update(new_elem)
