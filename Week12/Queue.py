# Queue
from pydantic import *
from typing import *


class Queue():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.front = None
        self.rear = -1
        self.queue = [None] * capacity

    def enqueue(self, item) -> None:
        ''''
            Добавляет элемент в конец очереди
        '''
        if self.is_full():
            raise OverflowError('Queue is full')
        if self.front is None:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self) -> Any:
        ''''
            Удаляет и возвращает первый элемент из очереди
        '''
        if self.is_empty():
            raise IndexError('Queue is empty')
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = None
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def peek(self) -> Any:
        '''
            Возвращает первый элемент из очереди, но не удаляет его
        '''
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.queue[self.front]

    def is_empty(self) -> bool:
        return self.front is None

    def is_full(self) -> bool:
        return self.front == (self.rear + 1) % self.capacity


q = Queue(capacity=2)
assert True == q.is_empty()
q.enqueue(1)
q.enqueue(2)
assert True == q.is_full()
print(q.peek())
print(q.dequeue())
print(q.dequeue())
assert True == q.is_empty()
