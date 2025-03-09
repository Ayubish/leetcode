class MyQueue:

    def __init__(self):
        self.stack = []
        self.cursor = 0
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.cursor != len(self.stack):
            el = self.stack[self.cursor]
            self.cursor += 1
            return el

    def peek(self) -> int:
        if self.cursor != len(self.stack):
            return self.stack[self.cursor]

    def empty(self) -> bool:
        if self.cursor == len(self.stack):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()