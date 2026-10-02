from typing import List

class ListNode:
    def __init__(self, val, next_node=None) -> None:
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)   # dummy node
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next      # skip the dummy
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next
            if curr.next is None:
                self.tail = curr
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals