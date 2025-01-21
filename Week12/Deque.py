# Deque
from pydantic import *
from typing import *


class Deque():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.front = None
        self.rear = capacity
        self.queue = [None] * capacity
        self.size = 0

    def add_front(self, item) -> None:
        # if self.is_full():
        #     raise OverflowError('Queue is full')
        if self.front is None:
            self.front = 0
        else:
            self.front = (self.front + 1) % self.capacity
        self.queue[self.front] = item
        self.size += 1

    def add_rear(self, item) -> None:
        if self.is_full():
            raise OverflowError('Queue is full')
        self.rear = (self.rear - 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def remove_rear(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        item = self.queue[self.rear]
        self.queue[self.rear] = None
        self.rear = (self.rear + 1) % self.capacity
        self.size -= 1
        return item

    def remove_front(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front - 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

d = Deque(4) #[1, 2, 4, 3]
d.add_rear(3)
d.add_rear(4)
d.add_front(1)
d.add_front(2)
assert d.is_full() == True
print(d.queue)
print(d.remove_front())
print(d.remove_front())
print(d.remove_rear())
print(d.remove_rear())
print(d.queue)
assert d.is_empty() == True
