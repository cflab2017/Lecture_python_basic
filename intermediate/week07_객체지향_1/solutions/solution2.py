class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.peek())
print(len(s))
print(s.pop())
print(s.pop())
print(s.is_empty())
print(s.pop())
print(s.is_empty())
