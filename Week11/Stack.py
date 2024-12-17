from pydantic import *
from typing import Optional

from Structures.LinkedList import Node, LinkedList

class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    # Добавляет в начало
    def push(self, val: str) -> None:
        self.append(val)

    # Удаляет верхний элемент из стека
    def pop(self) -> None:
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    # Выводим верхний элемент
    def peek(self) -> str:
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        current = self.head
        while current.next:
            current = current.next
        return current.val
    def is_empty(self) -> bool:
        return self.head is None




s = Stack()
print(s.is_empty()) # True
s.append('First')
s.append('Second')
s.append('Third')
print(s.is_empty()) # False
print('before pop', s)
s.pop()
print('after pop', s)
print('peeked', s.peek())

# True
# False
# before pop head=Node(val='First', next=Node(val='Second', next=Node(val='Third', next=None)))
# after pop head=Node(val='First', next=Node(val='Second', next=None))
# peeked Second