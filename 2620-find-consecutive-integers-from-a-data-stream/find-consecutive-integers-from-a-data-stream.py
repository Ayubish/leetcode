class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.val = value
        self.k = k
        self.count = 0
    def consec(self, num: int) -> bool:
        if len(self.queue) == self.k:
            popped = self.queue.popleft()
            if popped == self.val:
                self.count -= 1
        self.queue.append(num)
        if num == self.val:
            self.count += 1
        if len(self.queue)==self.k:
            if self.count == self.k:
                return True
        return False
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)