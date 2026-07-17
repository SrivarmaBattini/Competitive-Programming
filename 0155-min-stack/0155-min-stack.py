class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        
        curr_min = min(self.stack[-1][1], value) if self.stack else value
        self.stack.append([value, curr_min])

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        else:
            return []

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()