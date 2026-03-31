class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.data
            current = current.next
            i += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        print(self.head.data,'Head')
        print(self.tail.data,'Tail')
        print(self.getValues(),'ss')
        

    def remove(self, index: int) -> bool:
        if self.head is None: return False
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        prev = None
        current = self.head
        i = 0
        while current:
            if i == index:
                prev.next = current.next
                if prev.next is None: self.tail = prev
                return True
            prev = current
            current = current.next
            i+=1
        return False


    def getValues(self) -> List[int]:
        val_list = []
        current = self.head
        if current is None:
            return val_list
        while current:
            if current.data is not None:
                val_list.append(current.data)
            current = current.next
        return val_list
        
