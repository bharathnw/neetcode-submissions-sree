class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
class LinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.store = {}

    
    def add(self, key):
        tail = self.tail
        node = ListNode(key, tail.prev, tail)
        self.store[key] = node
        node.prev.next = node
        tail.prev = node

    def popLeft(self):
        head = self.head
        curr = self.head.next
        nxt = curr.next
        head.next = nxt
        nxt.prev = head
        self.store.pop(curr.val, None)
        return curr.val
    
    def popKey(self, key):
        if key in self.store:
            node = self.store.pop(key)
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
    
    def update(self, key):
        if key in self.store:
            node = self.store[key]
            left = node.prev
            right = node.next
            left.next = right
            right.prev = left
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.cache = {}
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        currentCnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[currentCnt].popKey(key)
        self.listMap[currentCnt+1].add(key)

        if self.minFreq == currentCnt and len(self.listMap[currentCnt].store) == 0:
            self.minFreq += 1
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return
        
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return

        if len(self.cache) >= self.capacity:
            res = self.listMap[self.minFreq].popLeft()
            self.countMap.pop(res)
            self.cache.pop(res)
        
        self.cache[key] = value
        self.countMap[key] = 1
        self.listMap[1].add(key)
        self.minFreq = 1