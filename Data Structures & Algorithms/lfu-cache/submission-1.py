class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class ListNode:

    def __init__(self):
        self.nodePointer = {}
        self.head = Node(0)
        self.tail = Node(0, self.head)
        self.head.next = self.tail
    
    def length(self):
        return len(self.nodePointer)

    def add(self, val):
        curr = self.tail.prev
        newNode = Node(val, curr, self.tail)
        curr.next = newNode
        self.tail.prev = newNode
        self.nodePointer[val] = newNode
    
    def remove(self, val):
        node = self.nodePointer[val]
        self.nodePointer.pop(val)
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def findFirst(self):
        head = self.head
        return head.next
    
    def removeFirst(self):
        node = self.findFirst()
        self.remove(node.val)
        return node.val


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.counter = defaultdict(ListNode)
        self.counterMap = defaultdict(int)
        self.capacity = capacity
        self.minCap = 0

    def counterFn(self, key):
        cnt = self.counterMap[key]
        self.counterMap[key] += 1
        if cnt > 0:
            self.counter[cnt].remove(key)
        self.counter[cnt+1].add(key)
        if cnt == self.minCap and self.counter[cnt].length() == 0:
            self.minCap += 1


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.counterFn(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                res = self.counter[self.minCap].removeFirst()
                self.counterMap.pop(res)
                self.cache.pop(res)
            self.cache[key] = value
            self.counterMap[key] = 0
            self.minCap = 1
            self.counterFn(key)
        else:
            self.cache[key] = value
            self.counterFn(key)