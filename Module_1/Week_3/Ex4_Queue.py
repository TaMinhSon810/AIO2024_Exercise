class MyQueue:
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity

    def is_full(self):
        return len(self._data) == self._capacity

    def enqueue(self, value):
        if self.is_full():
            print("Do nothing!")
        else:
            self._data.append(value)

    def is_empty(self):
        return len(self._data) == 0

    def dequeue(self):
        if self.is_empty():
            print("Do nothing!")
        else:
            return self._data.pop(0)

    def front(self):
        return self._data[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
