class MyStack:
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity

    def is_full(self):
        return len(self._data) == self._capacity

    def push(self, value):
        if self.is_full():
            print("Do nothing!")
        else:
            self._data.append(value)

    def is_empty(self):
        return len(self._data) == 0

    def pop(self):
        if self.is_empty():
            print("Do nothing!")
        else:
            return self._data.pop()

    def top(self):
        return self._data[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)

print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
