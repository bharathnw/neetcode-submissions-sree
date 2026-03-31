class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 'haed')
        self.tail = ListNode(0, 'tail')
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = ListNode(value, key)
            self.remove(self.cache[key])
            self.add(node)
            self.cache[key] = node
            return 
        self.cache[key] = ListNode(value, key)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            rm = self.head.next
            self.remove(rm)
            del self.cache[rm.key]


        
      


        
