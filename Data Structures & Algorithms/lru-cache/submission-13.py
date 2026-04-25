class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head  
        self.capacity = capacity      
    
    def remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
    
    def update(self, node, val):
        self.remove(node)
        prev = self.tail.prev
        newNode = ListNode(node.key, val)
        prev.next = newNode
        newNode.next = self.tail
        self.tail.prev = newNode
        newNode.prev = prev
        self.cache[node.key] = newNode

    def get(self, key: int) -> int:

        if key in self.cache:
            self.update(self.cache[key], self.cache[key].val)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.update(self.cache[key], value)
            return
        node = ListNode(key, value)
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev
        self.cache[key] = node
        if self.capacity < len(self.cache):
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
            




        
