class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.k = k

        

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        if self.size == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
        self.size += 1
        return True
        
        

    def deQueue(self) -> bool:
        if self.size > 0:
            curr = self.head
            self.size -= 1
            if self.size == 0:
                self.head = None
                self.tail = None
                return True
            if curr and curr.next:
                self.head = curr.next
            return True
        return False
        

    def Front(self) -> int:
        if self.size > 0 and self.head:
            return self.head.val
        return -1
        

    def Rear(self) -> int:
        if self.size > 0 and self.tail:
            return self.tail.val
        
        return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()