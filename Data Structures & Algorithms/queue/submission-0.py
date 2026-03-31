class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:
    
    def __init__(self):
        self.head = ListNode('head')
        self.tail = ListNode('tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        print(self.head.next.val == 'tail')
        return self.head.next.val == 'tail'

    def append(self, value: int) -> None:
        node = ListNode(value)
        prevNode = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        prevNode.next = node
        node.prev = prevNode

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        nextNode.prev = node
        node.next = nextNode

    def pop(self) -> int:
        if self.isEmpty(): return -1
        currentTail = self.tail.prev
        prevTail = currentTail.prev
        prevTail.next = self.tail
        self.tail.prev = prevTail
        return currentTail.val
        

    def popleft(self) -> int:
        if self.isEmpty(): return -1
        currentHead = self.head.next
        nextHead = currentHead.next
        self.head.next = nextHead
        nextHead.prev = self.head
        return currentHead.val
        
