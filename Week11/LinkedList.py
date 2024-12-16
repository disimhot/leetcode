# LinkedList
from pydantic import *
from typing import Optional
class Node(BaseModel):
    val: str
    next: Optional['Node'] = None

class LinkedList(BaseModel):
    head: Optional[Node] = None

    def append(self, val: str) -> None:
        if self.head is None:
            self.head = Node(val=val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val=val)

    def prepend(self, val: str) -> None:
        node = Node(val=val)
        node.next = self.head
        self.head = node

    def delete(self, val: str) -> None:
        # Удаляю первое встретившееся значение
        current = self.head
        prev = None
        while current and current.val != val:
            prev = current
            current = current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def display(self) -> None:
        current = self.head
        while current:
            print(current.val)
            current = current.next



# create linked list
linked_list = LinkedList()
linked_list.append("First")
linked_list.append("Second")
linked_list.prepend("Third")
linked_list.prepend("First")

linked_list.delete("Noexist")

linked_list.display()


