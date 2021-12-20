class MinStack:

    def __init__(self):
        #self.top = -1
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        n = len(self.stack)
        del self.stack[n-1]

    def top(self) -> int:
        a = self.stack[len(self.stack)-1]
        return a

    def getMin(self) -> int:
        a = min(self.stack)
        return a        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
