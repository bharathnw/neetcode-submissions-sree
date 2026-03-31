"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        mapKey = {None: None}
        while curr:
            copy = Node(curr.val)
            mapKey[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = mapKey[curr]
            copy.next = mapKey[curr.next]
            copy.random = mapKey[curr.random]
            curr = curr.next

        return mapKey[head]


