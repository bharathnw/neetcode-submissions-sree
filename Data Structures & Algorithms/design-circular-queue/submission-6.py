class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.size >= self.cap:
            return False
        
        node = ListNode(value)
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.size > 0:
            nxt = self.head.next
            next_nxt = nxt.next
            self.head.next = next_nxt
            next_nxt.prev = self.head
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.size == 0:
            return -1
        nxt = self.head.next
        return nxt.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        prev = self.tail.prev
        return prev.val

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()